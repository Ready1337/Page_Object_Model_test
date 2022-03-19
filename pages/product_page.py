from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    def click_add_to_basket(self):
        basket = self.browser.find_element(*self.locators.ADD_TO_BASKET_BUTTON)
        basket.click()
