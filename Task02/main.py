from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure, OperationFailure

# Налаштування підключення до MongoDB
client = MongoClient('mongodb+srv://new28:<password>@cluster28.syu8jlg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster28')

try:
   client.admin.command('ping')
except ConnectionFailure:
    print("Сервер MongoDB не доступний")
    exit(1)  # Вихід з програми у разі недоступності сервера

db = client['cats_db']
collection = db['cats_collection']

# Функції CRUD

def create_cat(name, age, features):
    """Створює новий запис про кота."""
    try:
        cat_id = collection.insert_one({
            "name": name,
            "age": age,
            "features": features
        }).inserted_id
        print(f"Кіт доданий з ID: {cat_id}")
    except OperationFailure as e:
        print(f"Помилка при додаванні кота: {e}")

def read_all_cats():
    """Виводить всі записи з колекції."""
    try:
        for cat in collection.find():
            print(cat)
    except OperationFailure as e:
        print(f"Помилка при читанні даних: {e}")

def read_cat_by_name(name):
    """Виводить інформацію про кота за іменем."""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кіт не знайдений.")
    except OperationFailure as e:
        print(f"Помилка при читанні даних: {e}")

def update_cat_age(name, new_age):
    """Оновлює вік кота за іменем."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Вік кота оновлено.")
        else:
            print("Кіт не знайдений або вік уже встановлено.")
    except OperationFailure as e:
        print(f"Помилка при оновленні даних: {e}")

def add_feature_to_cat(name, feature):
    """Додає нову характеристику до кота за іменем."""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count:
            print("Характеристика додана.")
        else:
            print("Кіт не знайдений.")
    except OperationFailure as e:
        print(f"Помилка при оновленні даних: {e}")

def delete_cat_by_name(name):
    """Видаляє запис про кота за іменем."""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("Кіт видалений.")
        else:
            print("Кіт не знайдений.")
    except OperationFailure as e:
        print(f"Помилка при видаленні даних: {e}")

def delete_all_cats():
    """Видаляє всі записи з колекції."""
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} котів.")
    except OperationFailure as e:
        print(f"Помилка при видаленні даних: {e}")

# Приклад використання функцій
create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
read_all_cats()
read_cat_by_name("Barsik")
update_cat_age("Barsik", 4)
add_feature_to_cat("Barsik", "любить сметану")
delete_cat_by_name("Barsik")
delete_all_cats()
