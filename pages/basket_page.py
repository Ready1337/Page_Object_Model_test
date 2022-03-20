from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    locators = BasketPageLocators()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(self.locators.BASKET_PRODUCTS), \
            'Products in basket are presented but should not be'

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(self.locators.BASKET_EMPTY_MESSAGE), \
            'Text about empty basket is not presented but should be'

    def should_be_empty_basket(self):
        self.should_not_be_products_in_basket()
        self.should_be_text_about_empty_basket()
