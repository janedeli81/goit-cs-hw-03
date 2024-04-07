from faker import Faker
import psycopg2
import random

faker = Faker()

# Підключення до бази даних
conn = psycopg2.connect(
    dbname='your_dbname', user='your_user',
    password='your_password', host='your_host'
)
cur = conn.cursor()

# Створення випадкових користувачів
for _ in range(10):
    fullname = faker.name()
    email = faker.email()
    cur.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;",
        (fullname, email)
    )

# Створення випадкових завдань
for _ in range(30):
    title = faker.sentence(nb_words=6)
    description = faker.text(max_nb_chars=200)
    status_id = random.randint(1, 3)
    user_id = random.randint(1, 10)
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
        (title, description, status_id, user_id)
    )

conn.commit()

# Закриття з'єднання
cur.close()
conn.close()
