import allure
from methods.courier_methods import CourierMethods
from data import *
import pytest


class TestCourierLogin:
    @allure.title('Проверяем что курьер может авторизоваться')
    @allure.description('Передаем логин и пароль.')
    def test_create_courier_success(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier(login_pass)
        assert r.status_code == 200
        assert r.json()['id'] == courier_methods.get_courier_id(login_pass)

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе несуществующей пары логина и пароля')
    @allure.description('Передаем данные без логина или пароля.')
    @pytest.mark.parametrize('payload', InvalidDataForLogin.payloads)
    def test_create_courier_account_with_empty_required_fields(self, payload):
        courier_methods = CourierMethods()
        r = courier_methods.post_login_courier(payload)
        assert r.status_code == 404
        assert Errors.ERROR_LOGIN_404_NO_SUCH_USER in r.json()['message']

    @allure.title('Проверка получения ошибки при логине курьера без пароля')
    @allure.description('Передаем данные без пароля.')
    def test_create_courier_account_without_password(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier_without_password(login_pass)
        assert r.status_code == 400
        assert Errors.ERROR_LOGIN_400_NO_LOGIN_OR_PASS in r.json()['message']

    @allure.title('Проверка получения ошибки при логине курьера без логина')
    @allure.description('Передаем данные без логина.')
    def test_create_courier_account_without_login(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier_without_login(login_pass)
        assert r.status_code == 400
        assert Errors.ERROR_LOGIN_400_NO_LOGIN_OR_PASS in r.json()['message']
