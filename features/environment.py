from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    Initialize the browser and the Application object.
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    context.driver = webdriver.Chrome()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    """
    This hook will be executed before each step.
    """
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
def before_step(context, step):
    """
    This hook will be executed before each step.
    """
    print('\nStarted step: ', step)
def after_step(context, step):
    """
    This hook will be executed after each step.
    """
    if step.status == 'failed':
        print('\nStep failed: ', step)
def after_scenario(context, feature):
    """
       This hook will be executed after each scenario.
       """
    if hasattr(context, 'driver') and context.driver:
        context.driver.delete_all_cookies()
        context.driver.quit()
