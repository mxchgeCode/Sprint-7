class URLs:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDERS_URL = '/api/v1/orders'
    COURIER_CREATE_URL = '/api/v1/courier'
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    DELETE_COURIER_URL = '/api/v1/courier/'
    CREATE_ORDERS_URL = '/api/v1/orders'
    GET_ORDER_BY_TRACK_URL = '/api/v1/orders/track?t='


class OrderData:
    order_data_black = {
        "firstName": "Joann",
        "lastName": "Marcella",
        "address": "NY, Suite 578",
        "metroStation": 5,
        "phone": "85017591376",
        "rentTime": 1,
        "deliveryDate": "2025-01-01",
        "comment": "check my pizza",
        "color": [
            "BLACK"
        ]
    }
    order_data_grey = {
        "firstName": "Joann",
        "lastName": "Marcella",
        "address": "NY, Suite 578",
        "metroStation": 5,
        "phone": "85017591376",
        "rentTime": 1,
        "deliveryDate": "2025-01-01",
        "comment": "check my pizza",
        "color": [
            "GREY"
        ]}

    order_data_grey_black = {
        "firstName": "Joann",
        "lastName": "Marcella",
        "address": "NY, Suite 578",
        "metroStation": 5,
        "phone": "85017591376",
        "rentTime": 1,
        "deliveryDate": "2025-01-01",
        "comment": "check my pizza",
        "color": [
            "GREY", "BLACK"
        ]}

    order_data_without_color = {
        "firstName": "Joann",
        "lastName": "Marcella",
        "address": "NY, Suite 578",
        "metroStation": 5,
        "phone": "85017591376",
        "rentTime": 1,
        "deliveryDate": "2025-01-01",
        "comment": "check my pizza",
        "color": []
    }


class Errors:
    ERROR_LOGIN_400_NO_LOGIN_OR_PASS = "Недостаточно данных для входа"
    ERROR_LOGIN_404_NO_SUCH_USER = "Учетная запись не найдена"

    ERROR_CREATE_400_NO_DATA = "Недостаточно данных для создания учетной записи"
    ERROR_CREATE_409_ALREADY_EXIST = "Этот логин уже используется"

    ERROR_DELETE_400_NO_DATA = "Недостаточно данных для удаления курьера"
    ERROR_DELETE_404_NO_SUCH_ID = "Курьера с таким id нет."

    ERROR_COUNT_ORDERS_NO_DATA = "Недостаточно данных для поиска"
    ERROR_COUNT_ORDERS_NO_SUCH_USER = "Курьер не найден"

    ERROR_TRACK_ORDER_NO_DATA = "Недостаточно данных для поиска"
    ERROR_TRACK_ORDER_NO_SUCH_ORDER = "Заказ не найден"

    ERROR_ACCEPT_ORDER_NO_ORDER_NUMBER = "Недостаточно данных для поиска"
    ERROR_ACCEPT_ORDER_NO_SUCH_COURIER = "Курьера с таким id не существует"
    ERROR_ACCEPT_ORDER_NO_DATA = "Недостаточно данных для поиска"


class InvalidDataForRegistration:
    payloads = [
        {
            'login': 'test_123_test',
            'password': '',
            'first_name': 'zzzzz',
        },
        {
            'login': '',
            'password': 'test_123_test',
            'first_name': 'zzzzz',
        }
    ]


class InvalidDataForLogin:
    payloads = [['xxxxx', 'zzzzz'], ['vvvvvv', 'bbbbbbb']]
