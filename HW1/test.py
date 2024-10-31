
from faker import Faker
import requests


fake = Faker()

URL = 'http://195.133.27.184/signup/'

def generate_registration_data():
    password = fake.password()
    return {
    'Имя пользователя': fake.user_name(),
    'Password': password,
    'Password confirmation': password
    }

def submit_registration_form(data):
    response = requests.post(URL, data=data)
    if response.status_code == 200:
        print("Все ОК!")
    else:
        print("Все не ОК:", response.status_code, response.text)

# запуск
if __name__ == "__main__":
    data = generate_registration_data()
    print("Отправка данных:", data)
    submit_registration_form(data)