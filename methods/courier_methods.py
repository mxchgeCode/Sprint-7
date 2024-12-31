import requests
from data import *
import allure


class CourierMethods:
    @allure.step("Cоздать курьера")
    def post_create_courier(self, payload):
        r = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_CREATE_URL}', data=payload)
        return r

    @allure.step("Попытка создать курьера со старым login_pass")
    def post_create_courier_with_old_login_pass(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1],
            'first_name': login_pass[2],
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_CREATE_URL}', data=payload)
        return response

    @allure.step("Вход с учетными данными login_pass")
    def post_login_courier(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1],
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_LOGIN_URL}', json=payload)
        return response

    @allure.step("Вход с учетными данными login_pass c пустым паролем")
    def post_login_courier_without_password(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': ''
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_LOGIN_URL}', data=payload)
        return response

    @allure.step("Вход с учетными данными login_pass с пустым логином")
    def post_login_courier_without_login(self, login_pass):
        payload = {
            'login': '',
            'password': login_pass[1]
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_LOGIN_URL}', data=payload)
        return response

    @allure.step("Получить id курьера")
    def get_courier_id(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1],
        }
        log_in_response = requests.post(f'{URLs.BASE_URL}{URLs.COURIER_LOGIN_URL}', data=payload)
        return log_in_response.json()['id']

    @allure.step("Удалить курьера")
    def delete_courier(self, login_pass):
        courier_id = self.get_courier_id(login_pass)
        requests.delete(f'{URLs.BASE_URL}{URLs.DELETE_COURIER_URL}{courier_id}')
