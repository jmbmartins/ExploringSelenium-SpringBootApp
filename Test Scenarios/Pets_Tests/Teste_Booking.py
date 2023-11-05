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

def enter_Booking(driver):
    try:
        driver.get('http://localhost:8080/mainpageclient')
        btn_Booking=driver.find_element(By.XPATH,'/html/body/div/div[2]/ul/li[1]/a')
        btn_Booking.click()
        url=driver.current_url
        if('http://localhost:8080/vcbooking' in url):
            print("** Test: Enter Page **")
            print("Status: Passed ")
            return True
        else:
            print("** Test: Enter Page **")
            print("Status: Failed")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")


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
   
def remove_Booking(driver):
    try:
        row_with_teste_nome = driver.find_element(By.XPATH, "//tr[td[5][contains(text(), 'teste_nome')]]")
        delete_button = row_with_teste_nome.find_element(By.XPATH, ".//td[6]/a")   
        delete_button.click()
        url=driver.current_url
        if('http://localhost:8080/vcbooking' in url):
            print("** Test: Delete **")
            print("Status: Passed ")
            return True
        else:
            print("** Test: Delete **")
            print("Status: Failed")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def doBooking(driver):
    try:
        driver.get('http://localhost:8080/showVCNewBookingForm')
        In_data_input = driver.find_element(By.ID,'checkInDate')
        In_data_input.clear()
        In_data_input.send_keys('07-11-2024')
        In_data_input2 = driver.find_element(By.ID,'checkOutDate')
        In_data_input2.clear()
        In_data_input2.send_keys('12-11-2024')
        select_element1 = driver.find_element(By.ID,'petId')
        select1 = Select(select_element1)
        select1.select_by_visible_text('teste_nome')
        select_element2 = driver.find_element(By.ID,'roomTypeSelect')
        select2 = Select(select_element2)
        select2.select_by_visible_text('Standard')
        btn_Booking=driver.find_element(By.XPATH,'/html/body/form/button')
        btn_Booking.click()
        url=driver.current_url
        if('http://localhost:8080/vcbooking' in url):
            print("** Test: Booking **")
            print("Status: Passed ")
            return True
        else:
            print("** Test: Booking **")
            print("Status: Failed ")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")

     
def enter_Reserve(driver):
    try:
        driver.get('http://localhost:8080/vcbooking')
        btn_Booking=driver.find_element(By.XPATH,'/html/body/a[2]')
        btn_Booking.click()
        url=driver.current_url
        if('http://localhost:8080/showVCNewBookingForm' in url):
            Pass=False
            Pass = doBooking(driver)
            if(Pass):
                url=driver.current_url
                if('http://localhost:8080/vcbooking' in url):
                    print("** Test: Booking **")
                    print("Status: Passed ")
                    return True
                else:
                    print("** Test: Booking **")
                    print("Status: Failed")
                    return False
        else:
            print("** Test: Booking **")
            print("Status: Failed ")
            return False 
    except Exception as e:
        print(f"An error occurred: {str(e)}")       

def main():
    try:
        os.environ['PATH'] += r";C:\SeleniumDrivers" 
        driver = webdriver.Chrome()
        driver.get('http://localhost:8080/')
        Pass = False
        Pass = Login_User(driver)
        if Pass:
            Pass=enter_Booking(driver)
        else:
            print("Stopping Tests!") 
        if Pass:
            Pass=enter_Reserve(driver)
        else:
            print("Stopping Tests!")
        if Pass:
            Pass=remove_Booking(driver)
        else:
            print("Stopping Tests!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()  # Close the browser

if __name__ == "__main__":
    main()
