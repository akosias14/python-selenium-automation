from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
    def open_url(self, url):
        if self.driver is None:
            raise ValueError("Driver is not initialized")
        self.driver.get(url)
    def click_cart_icon(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/CartLink']"))).click()


