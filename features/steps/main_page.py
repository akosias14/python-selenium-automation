import time
from behave import given, when, then
@given('open target webpage "{url}"')
def open_url(context, url):
    if context.app is None:
        raise Exception("Application has not been initialized")
    context.app.main_page.open_url('https://www.target.com/')

@when('the user clicks on the Cart icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()
    time.sleep(3)
@then('verify that the user see the message Your cart is empty')
def verify_see_the_message(context):
    context.app.cart_page.verify_see_the_message()
    time.sleep(5)

