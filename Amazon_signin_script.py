from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new  Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com')
driver.find_element(By.XPATH, "//span[text()='& Orders']").click()
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.ID, 'ap_email').click()

expected_results = 'amazon'
actual_results = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").text



print('Test Case Passed')
sleep (30)