import requests
from faker import Faker
from bs4 import BeautifulSoup

fake = Faker()

URL = 'http://195.133.27.184/signup/'


def generate_registration_data(csrf_token):
    password = fake.password()
    return {
        'username': fake.user_name(),
        'password1': password,
        'password2': password,
        'csrfmiddlewaretoken': csrf_token
    }


def get_csrf_token(session):
    response = session.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        return csrf_token
    else:
        print("Не удалось получить CSRF-токен.")
        return None


# отправляем данные на сервер
def submit_registration_form(session, data):
    headers = {
        'Referer': URL
    }
    response = session.post(URL, data=data, headers=headers)
    if response.status_code == 200:
        print("Все ОК!")
    else:
        print("Все совсем не ОК:", response.status_code, response.text)


# запуск
if __name__ == "__main__":
    # cookies
    session = requests.Session()

    # Получение CSRF-токена
    csrf_token = get_csrf_token(session)
    if csrf_token:
        # Генерация данных регистрации с CSRF-токеном
        data = generate_registration_data(csrf_token)
        print("Отправка данных:", data)

        # Отправка данных на сервер
        submit_registration_form(session, data)
