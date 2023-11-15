from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open target web page')
def open_target(context):
    context.driver.get('https://www.target.com/')

sleep(2)

@when('the user clicks on the Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


sleep(3)

@then('verify that the user see the message "Your cart is empty"')
def see_the_message(context):
    try:
        empty_message = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']")
        assert empty_message.is_displayed(), 'Empty message is not displayed'
    except NoSuchElementException:
        assert False, 'Empty not found'
sleep(3)

print('Empty message is displayed')



