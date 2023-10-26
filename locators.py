from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

#by XPATH Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#by ID Email Field
driver.find_element(By.ID, 'ap_email')

#by XPATH Email Field
driver.find_element(By.XPATH, "//input[@type='email']")

#by XPATH continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

#by XPATH need help
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#by XPATH forgot password link
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")

#by XPATH other issues with sign in
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")

 #by ID other issues with sign in
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#by Xpath Create your Amazon account button
driver.find_element(By.XPATH, "//a[@class='a-button-text']")

#by Xpath *Conditions of use link
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-top-medium a-size-small']//a[text()='Conditions of Use']")

#by Xpath Privacy Notice link
driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-top-medium a-size-small']//a[text()='Privacy Notice']")
