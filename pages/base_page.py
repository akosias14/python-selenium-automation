from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)


    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)
        pass

    def wait_for_element_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(*locator), message=f'Element by {locator} not clickable').click()

    def wait_for_element_appear(self, *locator):
        element = self.wait.until(EC.visibility_of_element_located(*locator), message=f'Element by {locator} not visible')
        return element
