import pytest
import time

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time()) + '1234567890'
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.skip('skip')
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.skip('skip')
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_basket()
        product_page.should_be_success_message()


@pytest.mark.skip('skip')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.skip('skip')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.should_not_be_success_message_with_disappeared()


@pytest.mark.skip('skip')
def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.skip('skip')
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip('skip')
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    products_page = ProductPage(browser, link)
    products_page.open()
    products_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
