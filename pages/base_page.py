from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

from pages.locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        link = self.browser.find_element(*self.locators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*self.locators.BASKET_LINK)
        link.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

    def should_be_login_link(self):
        assert self.is_element_present(self.locators.LOGIN_LINK), \
            'Login link is not presented'

    def should_be_authorized_user(self):
        assert self.is_element_present(self.locators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
