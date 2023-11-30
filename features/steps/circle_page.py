from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given("I am on the Target Circle page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")

@then("verify The 5 benefit boxes are visible")
def step_then_verify_benefit_boxes(context):
    benefit_boxes = context.driver.find_elements(By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc-9mx6dj-2 lgQxFm']")
    assert len(benefit_boxes) == 5, f"Expected 5 benefit boxes, but found {len(benefit_boxes)}"
