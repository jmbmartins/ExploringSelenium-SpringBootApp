import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

def Login_User(driver):
    try:
        driver.get('http://localhost:8080/login')
        btn_Login = driver.find_element(By.ID, 'btnSub')
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        email_input.send_keys('user1@example.com')
        password_input.send_keys('password1')
        btn_Login.click()
        url = driver.current_url
        if('http://localhost:8080/mainpageclient' in url):
            print("** Test: Login User  **")
            print("Status: Passed ")
            return True
        elif('?error=true' in url):
            print("** Test: Login User**")
            print("Status: Failed")
            print("Reason: Wrong User/Password")
            return False
    except Exception as e:
        print("** Test: Login User**")
        print("Status: Failed")
        print("Reason:", str(e))
        return False

def enter_Feeding(driver):
    try:
        driver.get('http://localhost:8080/mainpageclient')
        btn_Feeding=driver.find_element(By.XPATH,'/html/body/div/div[2]/ul/li[2]/a')
        btn_Feeding.click()
        url=driver.current_url
        if('http://localhost:8080/vcfeeding' in url):
            print("** Test: Enter Page **")
            print("Status: Passed ")
            return True
        else:
            print("** Test: Enter Page **")
            print("Status: Failed")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def doFood(driver):
    try:
        select_element = driver.find_element(By.ID,'petId')
        select = Select(select_element)
        select.select_by_visible_text('teste_nome')
        select_element2 = driver.find_element(By.ID,'type')
        select2 = Select(select_element2)
        select2.select_by_visible_text('Dry Food')
        btn_register=driver.find_element(By.XPATH,'/html/body/form/button')
        btn_register.click()
        url=driver.current_url
        if('http://localhost:8080/vcfeeding' in url):
            print("** Test: Regist Food **")
            print("Status: Passed ")
            return True
        else:
            print("** Test: Regist Food **")
            print("Status: Failed ")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
   
def removeFood(driver):
    try:
        row_with_teste_nome = driver.find_element(By.XPATH, "//tr[td[2][contains(text(), 'teste_nome')]]")
        delete_button = row_with_teste_nome.find_element(By.XPATH, ".//td[3]/a")   
        delete_button.click()
        url=driver.current_url
        if('http://localhost:8080/vcfeeding' in url):
            print("** Test: Delete **")
            print("Status: Passed ")
            return True
        else:
            print("** Test: Delete **")
            print("Status: Failed")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
     
def enter_Reserve(driver):
    driver.get('http://localhost:8080/vcfeeding')
    btn_Feeding=driver.find_element(By.XPATH,'/html/body/a[2]')
    btn_Feeding.click()
    url=driver.current_url
    if('http://localhost:8080/showVCNewFeedingForm' in url):
        Pass=False
        Pass = doFood(driver)
        if(Pass):
            url=driver.current_url
            if('http://localhost:8080/vcfeeding' in url):
                print("** Test: Feeding **")
                print("Status: Passed ")
                return True
            else:
                print("** Test: Feeding **")
                print("Status: Failed ")
                return False
        else:
           print("** Test: Feeding **")
           print("Status: Failed ")
           return False 
           
def main():
    try:
        os.environ['PATH'] += r";C:\SeleniumDrivers" 
        driver = webdriver.Chrome()
        driver.get('http://localhost:8080/')
        Pass = False
        Pass = Login_User(driver)
        if Pass:
            Pass=enter_Feeding(driver)
        else:
            print("Stopping Tests!") 
        if Pass:
            Pass=enter_Reserve(driver)
        else:
            print("Stopping Tests!")
        if Pass:
            Pass=removeFood(driver)
        else:
            print("Stopping Tests!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()  # Close the browser

if __name__ == "__main__":
    main()
