from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    def click_add_to_basket(self):
        basket = self.browser.find_element(*self.locators.ADD_TO_BASKET_BUTTON)
        basket.click()

    def get_product_name(self):
        return self.browser.find_element(*self.locators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.locators.PRODUCT_PRICE).text

    def should_be_product_name_in_success_message(self):
        product_name = self.browser.find_element(*self.locators.ALERT_PRODUCT_NAME).text
        assert product_name == self.get_product_name()

    def should_be_product_price_in_success_message(self):
        product_price = self.browser.find_element(*self.locators.ALERT_PRODUCT_PRICE).text
        assert product_price == self.get_product_price()

    def should_be_success_message(self):
        self.should_be_product_name_in_success_message()
        self.should_be_product_price_in_success_message()
