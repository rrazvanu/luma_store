from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPlacementPage(BasePage):
    SEARCH_ENTIRE_STORE_INPUT_FIELD = (By.ID, 'search')
    ADD_TO_CART_BUTTON = (By.ID, 'product-addtocart-button')
    MY_CART_BUTTON = (By.XPATH, 'My Cart')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//span[text()="Proceed to Checkout"]')
    CHECKOUT_NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//span[text()="Place Order"]')

    REQUIRED_FIELD_ERROR = (By.XPATH, '//div[text()="This is a required field."]')



    THANK_YOU_FOR_PURCHASES_MESSAGE = (By.XPATH, '//span[text()="Thank you for your purchase!"]')
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//span[text()="Continue Shopping"]')
    QUANTITY_INPUT_FIELD = (By.ID, 'qty')


    #quatity errors
    MAX_PURCHASE_1000_INFO_MESSAGE = (By.XPATH, '//div[text()="The maximum you may purchase is 10000."]')
    INVALID_VALUE_INFO_MESSAGE = (By.XPATH, '//div[text()="Please enter a quantity greater than 0."]')
    def search_entire_store(self, search_term):
        self.wait_for_elem(*self.SEARCH_ENTIRE_STORE_INPUT_FIELD)
        self.driver.find_element(*self.SEARCH_ENTIRE_STORE_INPUT_FIELD).send_keys(search_term)
        self.driver.find_element(*self.SEARCH_ENTIRE_STORE_INPUT_FIELD).send_keys('\n')

    def select_product(self, product_name):
        self.wait_for_elem(By.XPATH, f'//a[contains(., "{product_name}")]')
        self.driver.find_element(By.XPATH, f'//a[contains(., "{product_name}")]').click()

    def select_size(self, size):
        if size == 'S':
            size = 'option-label-size-143-item-166'
        if size == 'M':
            size = 'option-label-size-143-item-167'
        if size == 'L':
            size = 'option-label-size-143-item-168'
        if size == 'XL':
            size = 'option-label-size-143-item-169'
        self.wait_for_elem(By.ID, f'{size}')
        self.driver.find_element(By.ID, f'{size}').click()

    def select_color(self, color):
        color_locator = (By.XPATH, f'//div[@option-label="{color}"]')
        self.wait_for_elem(*color_locator)
        color_option = self.driver.find_element(*color_locator)
        color_option.click()

    def click_add_to_cart_button(self):
        self.wait_for_elem(*self.ADD_TO_CART_BUTTON)
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def open_my_cart(self):
        self.wait_for_elem(By.XPATH, '//a[@class="action showcart"]')
        self.driver.find_element(By.XPATH, '//a[@class="action showcart"]').click()

    def click_proceed_to_checkout_button(self):
        self.wait_for_elem(*self.PROCEED_TO_CHECKOUT_BUTTON)
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_checkout_next_button(self):
        self.wait_for_elem(*self.CHECKOUT_NEXT_BUTTON)
        self.driver.find_element(*self.CHECKOUT_NEXT_BUTTON).click()

    def click_place_order_button(self):
        self.wait_for_elem(*self.PLACE_ORDER_BUTTON)
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()

    def validate_order_complete(self):
        self.wait_for_elem(*self.THANK_YOU_FOR_PURCHASES_MESSAGE)
        assert self.driver.find_element(*self.THANK_YOU_FOR_PURCHASES_MESSAGE).is_displayed()
        order_number = self.driver.find_element(By.XPATH, '//p[text()="Your order number is: "]')
        assert order_number.is_displayed(), "Order number is not displayed"
        assert self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).is_displayed()

    def set_quantity(self, quantity):
        self.wait_for_elem(*self.QUANTITY_INPUT_FIELD)
        self.driver.find_element(*self.QUANTITY_INPUT_FIELD).clear()
        self.driver.find_element(*self.QUANTITY_INPUT_FIELD).send_keys(quantity)



    def validate_max_purchase_error_message(self):
        self.wait_for_elem(*self.MAX_PURCHASE_1000_INFO_MESSAGE)
        assert self.driver.find_element(*self.MAX_PURCHASE_1000_INFO_MESSAGE).is_displayed()


    def validate_invalid_value_error_message(self):
        self.wait_for_elem(*self.INVALID_VALUE_INFO_MESSAGE)
        assert self.driver.find_element(*self.INVALID_VALUE_INFO_MESSAGE).is_displayed()

    def validate_required_field_error_message(self):
        self.wait_for_elem(*self.REQUIRED_FIELD_ERROR)
        assert self.driver.find_element(*self.REQUIRED_FIELD_ERROR).is_displayed()