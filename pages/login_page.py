from selenium.webdriver.common.by import By

import config
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'pass')
    SIGN_IN_BUTTON = (By.ID, 'send2')
    MY_ACCOUNT_HEADER = (By.XPATH, '//h1[contains(., "My Account")]')

    def navigate_to_login_in_page(self):
        self.driver.get(config.url_base)

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.wait_for_elem(*self.PASSWORD_INPUT)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_sign_in_button(self):
        self.wait_for_elem(*self.SIGN_IN_BUTTON)
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def validate_login(self, user_name):
        welcome_message = self.driver.find_elements(By.XPATH, f'//span[contains(text(), "Welcome, {user_name}!")]')
        self.wait_for_elem(*welcome_message[0]), "The Welcome message is not displayed"
        self.wait_for_elem(*self.MY_ACCOUNT_HEADER)
        assert self.driver.find_element(
            *self.MY_ACCOUNT_HEADER).is_displayed(), 'The My Account header is not displayed'
        assert self.driver.find_element(*welcome_message[0]).is_displayed(), "The Welcome message is not displayed"

    def log_out(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/logout/')
