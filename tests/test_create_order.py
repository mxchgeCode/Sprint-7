import allure
from methods.order_methods import OrderMethods
from data import *
import pytest


class TestOrderCreate:

    @allure.title('Проверка создания заказа с разными значениями color')
    @allure.description('В тест передаются наборы данных с разными '
                        'параметрами: серый, черный, оба цвета, цвет не указан.')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_grey, OrderData.order_data_black,
        OrderData.order_data_grey_black, OrderData.order_data_without_color
    ])
    def test_order_create_color_success(self, order_data):
        order_methods = OrderMethods()
        r = order_methods.post_orders(order_data)
        assert r.status_code == 201 and 'track' in r.text
