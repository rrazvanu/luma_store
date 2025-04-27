from unittest import TestCase

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from browser import Browser


class BasePage(Browser, TestCase):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def verify_page_title(self, expected):
        actual = self.driver.title
        assert actual == expected, 'title is not correct'

    def verify_page_url(self, expected):
        actual = self.driver.current_url
        assert actual == expected, 'url is not correct'

    def navigate_to_home_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/')

    def navigate_to_my_cart(self):
        self.driver.get('https://magento.softwaretestingboard.com/checkout/cart/')