def make(client, title="Coffee", amount="10.00", category="food"):
    r = client.post(
        "/expenses/",
        json={"title": title, "amount": amount, "category": category},
    )
    assert r.status_code == 201, r.json()
    return r.json()

def test_create_and_get(client):
    e = make(client)
    r = client.get(f"/expenses/{e['id']}")
    assert r.status_code == 200
    assert r.json()["category"] == "food"


def test_get_404(client):
    assert client.get("/expenses/999").status_code == 404


def test_create_validation(client):
    r = client.post("/expenses/", json={"title": "x", "amount": "-5", "category": "food"})
    assert r.status_code == 422


def test_create_empty_title(client):
    r = client.post("/expenses/", json={"title": "", "amount": "5", "category": "food"})
    assert r.status_code == 422


def test_update(client):
    e = make(client)
    r = client.put(
        f"/expenses/{e['id']}",
        json={"title": "Rent", "amount": "99.99", "category": "rent"},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["title"] == "Rent"
    assert body["category"] == "rent"
    assert float(body["amount"]) == 99.99


def test_update_404(client):
    r = client.put("/expenses/999", json={"title": "x", "amount": "1", "category": "x"})
    assert r.status_code == 404


def test_delete(client):
    e = make(client)
    assert client.delete(f"/expenses/{e['id']}").status_code == 204
    assert client.get(f"/expenses/{e['id']}").status_code == 404


def test_filter_by_category(client):
    make(client, category="food")
    make(client, category="rent")
    r = client.get("/expenses/", params={"category": "food"})
    assert [x["category"] for x in r.json()] == ["food"]


def test_sort_by_amount_asc(client):
    make(client, amount="30")
    make(client, amount="10")
    make(client, amount="20")
    r = client.get("/expenses/", params={"sort_by": "amount", "order": "asc"})
    assert [float(x["amount"]) for x in r.json()] == [10, 20, 30]


def test_pagination(client):
    for i in range(5):
        make(client, amount=str(i + 1))
    r = client.get("/expenses/", params={"skip": 3, "limit": 10})
    assert len(r.json()) == 2


def test_invalid_sort_field_422(client):
    assert client.get("/expenses/", params={"sort_by": "hack"}).status_code == 422

def test_empty_summary(client):
    r = client.get('/expenses/summary')
    assert r.status_code==200
    body = r.json()
    assert float(body["total"]) == 0
    assert body['by_category'] == []

def test_summary_one_category(client):
    make(client, amount="10.00", category="food")
    make(client, amount="5.50", category="food")
    r = client.get("/expenses/summary")
    assert r.status_code == 200
    body = r.json()
    assert float(body["total"]) == 15.5
    assert len(body["by_category"]) == 1
    assert body["by_category"][0]["category"] == 'food'
    assert float(body["by_category"][0]["total"]) == 15.5