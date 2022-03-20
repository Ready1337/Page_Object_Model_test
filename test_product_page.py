import pytest

from pages.product_page import ProductPage


@pytest.mark.skip('skip')
@pytest.mark.parametrize(
    "url_suffix",
    [
        pytest.param("?promo=offer7", marks=pytest.mark.xfail) if i == 7 else f"?promo=offer{i}" for i in range(10)
    ]
)
def test_guest_can_add_product_to_basket(browser, url_suffix):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link + url_suffix)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()


@pytest.mark.skip('skip')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip('skip')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.should_not_be_success_message_with_disappeared()