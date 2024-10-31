from faker import Faker
import requests

# Создаем объект Faker
fake = Faker()

# URL регистрации
URL = 'http://localhost:5173/'

# Генерация данных
def generate_registration_data():
    return {
        'Имя': fake.user_name(),
        'Описание': fake.first_name(),
        'Шаги': fake.phone_number(),  # пример заполнения без запятой для упрощения
        'Ожидаемый результат': fake.phone_number(),
        'Приоритет': 'средний'
    }

# Отправка данных на сервер
def submit_registration_form(data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(URL, json=data, headers=headers)
    if response.status_code == 200:
        print("Регистрация прошла успешно!")
    else:
        print("Ошибка регистрации:", response.status_code, response.text)

# Запуск
if __name__ == "__main__":
    data = generate_registration_data()
    print("Отправляем данные:", data)
    submit_registration_form(data)

print("Отправка POST-запроса на:", URL)
response = requests.post(URL, json=data)
print("Код ответа:", response.status_code)
print("Текст ответа:", response.text)
