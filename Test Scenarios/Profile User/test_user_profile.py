import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://localhost:8080/')

try:
    email_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'btnSub')

    email_input.send_keys('manager@example.com')
    password_input.send_keys('managerpassword')
    login_button.click()

    time.sleep(2)

    driver.implicitly_wait(10)

    pagetitle_element = driver.find_element(By.ID, 'pagetitle')
    text = pagetitle_element.text

    assert "Welcome to Hotel Management Page" in text

    print("Test login administrator succeeded!")

except Exception as e:
    print("Test login administrator failed:", str(e))

try:
    driver.get('http://localhost:8080/')

    email_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'btnSub')

    email_input.send_keys('user1@example.com')
    password_input.send_keys('password1')
    login_button.click()

    time.sleep(2)
    
    driver.implicitly_wait(10)

    pagetitle_element = driver.find_element(By.ID, 'pagetitle')
    text = pagetitle_element.text

    assert "Welcome to Pet's Hotel," in text

    print("Test login client succeeded!")

except Exception as e:
    print("Test login client failed:", str(e))

finally:
    driver.quit()
