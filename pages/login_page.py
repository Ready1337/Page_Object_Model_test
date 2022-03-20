from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(self.locators.LOG_IN_EMAIL_ADDRESS_FIELD), \
            "Login email field is not presented"
        assert self.is_element_present(self.locators.LOG_IN_PASSWORD_FIELD), \
            "Login password field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(self.locators.REGISTRATION_EMAIL_ADDRESS_FIELD), \
            "Register email field is not presented"
        assert self.is_element_present(self.locators.REGISTRATION_PASSWORD_FIELD_1), \
            "Register first password field is not presented"
        assert self.is_element_present(self.locators.REGISTRATION_PASSWORD_FIELD_2), \
            "Register second password field is not presented"
