from faker import Faker
import requests

# Создаем объект Faker
fake = Faker()

# URL регистрации
URL = 'https://parabank.parasoft.com/parabank/register.htm;jsessionid=BBC92791D0AF4EEAB9DA25C2CECD2D8C'  # Замените на реальный URL для API регистрации, если отличается

# Генерация данных
def generate_registration_data():
    password = fake.password()  # Генерация случайного пароля
    return {
    'First Name': fake.first_name(),
    'Last Name': fake.last_name(),
    'Address': fake.address(),
    'City': fake.city(),
    'State': fake.state(),
    'Zip Code': fake.zipcode(),
    'Phone #': fake.phone_number(),
    'SSN': fake.passport_number(),
    'Username': fake.user_name(),
    'password': password,
    'Confirm': password
    }

# Отправка данных на сервер
def submit_registration_form(data):
    response = requests.post(URL, data=data)
    if response.status_code == 200:
        print("Регистрация прошла успешно!")
    else:
        print("Ошибка регистрации:", response.status_code, response.text)

# запуск
if __name__ == "__main__":
    data = generate_registration_data()
    print("Отправляем данные:", data)
    submit_registration_form(data)
# URL для авторизации (замените на реальный URL)
LOGIN_URL = 'https://parabank.parasoft.com/parabank/login.htm'


# Функция для отправки запроса на авторизацию
def login(username, password):
    login_data = {
        'username': username,
        'password': password
    }
    response = requests.post(LOGIN_URL, data=login_data)
    if response.status_code == 200 and "Welcome" in response.text:  # "Welcome" - предполагаемая часть текста на странице успешного входа
        print("Успешный вход, регистрация подтверждена!")
    else:
        print("Ошибка входа, регистрация не прошла:", response.status_code, response.text)


# запуск
if __name__ == "__main__":
    # Генерация данных регистрации
    data = generate_registration_data()
    print("Отправляем данные:", data)

    # Отправка данных на сервер
    submit_registration_form(data)

    # Проверка регистрации через авторизацию
    login(data['Username'], data['password'])

