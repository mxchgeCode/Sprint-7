import requests
from data import URLs
from faker import Faker


def register_new_courier_and_return_login_password():
    login_pass = []
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    first_name = fake.name()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_CREATE_URL}', data=payload)
    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['firstName'])
    return login_pass, response
