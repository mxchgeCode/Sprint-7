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
    error_login_400_no_login_or_pass = "Недостаточно данных для входа"
    error_login_404_no_such_user = "Учетная запись не найдена"

    error_create_400_no_data = "Недостаточно данных для создания учетной записи"
    error_create_409_already_exist = "Этот логин уже используется"

    error_delete_400_no_data = "Недостаточно данных для удаления курьера"
    error_delete_404_no_such_id = "Курьера с таким id нет."

    error_count_orders_no_data = "Недостаточно данных для поиска"
    error_count_orders_no_such_user = "Курьер не найден"

    error_track_order_no_data = "Недостаточно данных для поиска"
    error_track_order_no_such_order = "Заказ не найден"

    error_accept_order_no_order_number = "Недостаточно данных для поиска"
    error_accept_order_no_such_courier = "Курьера с таким id не существует"
    error_accept_order_no_data = "Недостаточно данных для поиска"


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
