import pytest
from helpers import *
from methods.courier_methods import CourierMethods


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture(scope='function')
def create_courier(courier_methods):
    login_pass, response = register_new_courier_and_return_login_password()
    yield login_pass, response
    courier_methods.delete_courier(login_pass)
