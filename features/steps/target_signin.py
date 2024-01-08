from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('clicks on the sign in button')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
sleep(2)

@then('Verify that the email field is present')
def email_field(context):
    try:
        email_field = context.driver.find_element(By.ID, 'username')
        assert email_field.is_displayed(), 'Email field is not displayed'
    except NoSuchElementException:
        assert False, 'Email field not found'
sleep(8)


print('Test case Pass')

