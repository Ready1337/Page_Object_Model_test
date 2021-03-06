from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    BASKET_LINK = (By.XPATH, '//span/a[contains(@href, "basket")]')


class LoginPageLocators(BasePageLocators):
    LOG_IN_EMAIL_ADDRESS_FIELD = (By.NAME, 'login-username')
    LOG_IN_PASSWORD_FIELD = (By.NAME, 'login-password')

    REGISTRATION_EMAIL_ADDRESS_FIELD = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD_FIELD_1 = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD_FIELD_2 = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')

    ALERT_PRODUCT_NAME = (By.XPATH, '//div[text()[contains(., "has been added to your basket")]]/strong')
    ALERT_PRODUCT_PRICE = (By.XPATH, '//p[text()[contains(., "Your basket total is now")]]/strong')

    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]/p[contains(@class, "price_color")]')

    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@id, "messages")]/div')


class BasketPageLocators(BasePageLocators):
    BASKET_PRODUCTS = (By.CSS_SELECTOR, '.basket-title')
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[contains(@id, "content_inner")]/p')
