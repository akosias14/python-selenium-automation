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
driver.get(https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26hvadid%3D675149237887%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9021702%26hvnetw%3Dg%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3De%26hvrand%3D11530931386108282327%26hvtargid%3Dkwd-10573980%26hydadcr%3D28883_14649097%26ref%3Dpd_sl_7j18redljs_e%26tag%3Damazusnavi-20%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0)

#amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo[aria-label="Amazon"]')
#Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Name
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')

#Email
driver.find_element(By.CSS_SELECTOR,'input#ap_email')

#Password
driver.find_element(By.CSS_SELECTOR,'input#ap_password')

#Passwords must be at least 6 characters
driver.find_element(By.CSS_SELECTOR,'div.a-box-inner.a-alert-container > div.a-alert-content')

#Re-enter Password
driver.find_element(By.CSS_SELECTOR,'input#ap_password_check.auth-required-field.auth-require-fields-match')

#Create Amazon Account
driver.find_element(By.CSS_SELECTOR,'input#a-autoid-0-announce.a-button-input')

#Conditions of use
driver.find_element(By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"]')

#Privacy Notice
driver.find_element(By.CSS_SELECTOR,'a[href="/gp/aw/help/ref=ap_mobile_register_notification_privacy_notice?id=468496"]')

#Sign In
driver.find_element(By.CSS_SELECTOR,'a.a-link-emphasis[href*="/ap/signin"]')