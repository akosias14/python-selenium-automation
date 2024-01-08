from selenium import webdriver
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage

class Application:
    def __init__(self, driver):
        if driver is None:
            raise ValueError("Driver should not be None")
        self.driver = driver
        self.cart_page = None
        self.initialize_pages()

    def initialize_pages(self):
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()



