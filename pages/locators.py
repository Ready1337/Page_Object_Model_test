from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_IN_EMAIL_ADDRESS_FIELD = (By.NAME, "login-username")
    LOG_IN_PASSWORD_FIELD = (By.NAME, "login-password")

    REGISTRATION_EMAIL_ADDRESS_FIELD = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_FIELD_1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_FIELD_2 = (By.NAME, "registration-password2")
