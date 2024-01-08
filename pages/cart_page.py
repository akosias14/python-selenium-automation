from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[class*='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']")
    EXPECTED_EMPTY_MSG = "Your cart is empty"
    def __init__(self, context):
        super().__init__(context)
    def verify_see_the_message(self):
        try:
            empty_message = self.driver.find_element(*self.EMPTY_CART_MSG)
            print(f"Actual message: '{empty_message.text}'")
            assert self.EXPECTED_EMPTY_MSG in empty_message.text, 'Expected message is not displayed'
        except NoSuchElementException:
            assert False,'Element for empty message not found'


