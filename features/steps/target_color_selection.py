from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
@given('Open target product A-88345426 page')
def step_given_user_on_product_page(context):
    context.driver.get('https://www.target.com/p/A-88345426')
    sleep(6)
@when('the user selects each color on the page')
def step_when_user_selects_each_color(context):
    expected_colors = ['Brown', 'Oatmeal', 'Gray', 'Black']
    actual_colors = []


    color_options = context.driver.find_elements(By.CSS_SELECTOR, '[class*="styles__ButtonWrapper-sc-519sqw-1 clSiPU"] img')
    for color_option in color_options:
        color_option.click()

@then('the selected color should be verified')
def step_then_verify_selected_color(context):
    selected_color_indicator = context.driver.find_element(By.CSS_SELECTOR, '[class*="styles__StyledBaseButtonInternal-sc-ysboml-0"][class*="BaseButtonSelector__StyledBaseButton-sc-dijc6i-0"][class*="iiyJUH"][class*="bIszwf"][class*="ButtonSelectorImage-sc-18tvdw-0"][class*="kZymTF"]')
    assert selected_color_indicator.is_displayed(), "Selected color is not displayed"

    def after_all(context):
        context.driver.quit()









