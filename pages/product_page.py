from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    def click_add_to_basket(self):
        basket = self.browser.find_element(*self.locators.ADD_TO_BASKET_BUTTON)
        basket.click()

    def get_product_name(self):
        return self.browser.find_element(*self.locators.PRODUCT_NAME).text

    def get_alert_product_name(self):
        return self.browser.find_element(*self.locators.ALERT_PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.locators.PRODUCT_PRICE).text

    def get_alert_product_price(self):
        return self.browser.find_element(*self.locators.ALERT_PRODUCT_PRICE).text

    def should_be_product_name_in_success_message(self):
        alert_product_name = self.get_alert_product_name()
        product_name = self.get_product_name()
        assert alert_product_name == product_name, \
            f'{product_name} is not presented in success message: {alert_product_name} instead'

    def should_be_product_price_in_success_message(self):
        alert_product_price = self.get_alert_product_price()
        product_price = self.get_product_price()
        assert alert_product_price == product_price, \
            f'{product_price} is not presented in success message: {alert_product_price} instead'

    def should_be_success_message(self):
        self.should_be_product_name_in_success_message()
        self.should_be_product_price_in_success_message()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(self.locators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def should_not_be_success_message_with_disappeared(self):
        assert self.is_disappeared(self.locators.SUCCESS_MESSAGE), \
            'Success message is not disappear but should be'
