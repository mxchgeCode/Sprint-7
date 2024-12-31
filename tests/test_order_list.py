import allure
from methods.order_methods import OrderMethods


class TestOrdersList:
    @allure.title('Проверка, что в тело ответа возвращается список заказов.')
    @allure.description('Получение списка заказов у метро ["1", "2"], проверка получения статуса кода 200 и списка '
                        'заказов в теле ответа длиной > 0.')
    def test_get_order_by_track_fast(self):
        order_methods = OrderMethods()
        r = order_methods.get_list_of_orders()
        assert r.status_code == 200 and len(r.json()["orders"]) > 0
