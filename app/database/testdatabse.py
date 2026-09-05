from database import engine, Base

try:
    with engine.connect() as conn:
        print("✅ Подключение успешно!")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")