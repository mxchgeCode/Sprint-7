import allure, pytest
from data import *
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_success(self, create_courier):
        login_pass, r = create_courier
        assert r.status_code == 201
        assert r.json() == {'ok': True}

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    @allure.description('Пытаемся создать двух одинаковых курьеров и проверяем код ответа и тело')
    def test_create_identical_couriers(self, create_courier):
        login_pass, _ = create_courier
        courier_methods = CourierMethods()
        r = courier_methods.post_create_courier_with_old_login_pass(login_pass)
        assert r.status_code == 409
        assert Errors.ERROR_CREATE_409_ALREADY_EXIST in r.json()['message']

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('Передаем данные без логина или пароля.''Проверяются код и тело ответа.')
    @pytest.mark.parametrize('payload', InvalidDataForRegistration.payloads)
    def test_create_courier_account_with_empty_required_fields(self, payload):
        courier_methods = CourierMethods()
        r = courier_methods.post_create_courier(payload)
        assert r.status_code == 400
        assert Errors.ERROR_CREATE_400_NO_DATA in r.json()['message']
