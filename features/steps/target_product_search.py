from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")






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

@given('open Target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')

@when('search for a {product}')
def step_when_search_product(context, product):
    search_box = context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    sleep(3)

@then('add {product} to the cart')
def add_to_cart(context, product):
    product_element = context.driver.find_element(By.XPATH, f'//a[@data-test="product-title" and contains(@aria-label, "{product}")]')
    product_element.click()  # Click on the product to add it to the cart

    # Now, find the "Add to Cart" button and click it
    add_to_cart_button = context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor82003666')
    add_to_cart_button.click()

    sleep(2)


@then('Verify that the {product} is in the cart')
def verify_product_in_cart(context, product):
    product_cart = context.driver.find_element(By.XPATH, '//a[@href="/cart" and contains(@class, "styles__StyledBaseButtonInternal") and contains(text(), "View cart & check out")]')
    product_cart.click()

    # Get the text content of the cart page
    cart_page_text = context.driver.find_element(By.XPATH, '//body').text

    assert product in cart_page_text, f'Expected text {product} not in {cart_page_text}'
    time.sleep(2)

    # Check if the cart has individual cart items or the total price (customize based on your preference)
    wait = WebDriverWait(context.driver, 15)
    cart_items = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-test="cartItem"]')))

    assert len(cart_items) > 0, "Product not found in the cart"

    print(f"Number of cart items found: {len(cart_items)}")


@when('search for {product}')
def step_when_search_for_product(context, product):
    search_box = context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()


@then('verify that every product has a name and an image')
def verify_all_product(context):
    context.driver.execute_script("window.scroll(0,2000)","")
    sleep(2)
    context.driver.execute_script("window.scroll(0,2000)", "")



    all_products = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    for product in all_products:
        title = product.find_element(By.CSS_SELECTOR, "[data-test='product-title']").text
        print(title)
        assert title.strip() != '', 'product title not shown'
        image_element = product.find_element(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")
        assert image_element.is_displayed(), 'Product image not shown'




