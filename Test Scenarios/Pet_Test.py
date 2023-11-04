import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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
def Test_Create_Pet(driver):
    try:
        driver.get('http://localhost:8080/showVCNewPetForm')
        age_input = driver.find_element(By.NAME, 'age')
        name_input = driver.find_element(By.NAME, 'name')
        race_input = driver.find_element(By.NAME, 'race')
        specie_input = driver.find_element(By.NAME, 'specie')
       
        save_btn = driver.find_element(By.ID, 'savePet')
        age_input.clear()
        age_input.send_keys('1')
        name_input.send_keys('teste_nome')
        race_input.send_keys('teste_raca')
        specie_input.send_keys('teste_especie')
        save_btn.click()
        url = driver.current_url
        if('http://localhost:8080/mainpageclient' in url):
            print("** Test: Create Pet  **")
            print("Status: Passed ")
            return True
    except Exception as e:
        print("** Test: Create Pet**")
        print("Status: Failed")
        print("Reason:", str(e))
        return False
def Test_Update_Pet(driver):
    try:
        driver.get('http://localhost:8080/mainpageclient')
        row_with_teste_nome = driver.find_element(By.XPATH, "//tr[td[2][contains(text(), 'teste_nome')]]")
        delete_button = row_with_teste_nome.find_element(By.XPATH, ".//td[5]/a[2]")   
        delete_button.click()
        url=driver.current_url
        if('http://localhost:8080/vcupdatepet/' in url):
            age_input = driver.find_element(By.NAME, 'age')
            age_input.clear()
            age_input.send_keys('2')
            botao = driver.find_element(By.XPATH, "/html/body/form/button")
            botao.click()
            url=driver.current_url
            if('http://localhost:8080/mainpageclient' in url):
                print("** Test: Delet Pet**")
                print("Status: Passed ")
                return True
            else:
                print("**Test:Update Pet")
                print("Status: Failed")
                return False
        else:
            print("**Test:Update Pet")
            print("Status: Failed")
            return False
    except Exception as e:
        print("** Test: Update Pet**")
        print("Status: Failed")
        print("Reason:", str(e))
        return False
def Test_Delete_Pet(driver):
    try:
        driver.get('http://localhost:8080/mainpageclient')
        row_with_teste_nome = driver.find_element(By.XPATH, "//tr[td[2][contains(text(), 'teste_nome')]]")
        delete_button = row_with_teste_nome.find_element(By.XPATH, ".//td[5]/a[1]")   
        delete_button.click()
        url=driver.current_url
        if('http://localhost:8080/mainpageclient' in url):
            print("** Test: Delete Pet**")
            print("Status: Passed ")
            return True
    except Exception as e:
        print("** Test: Delete Pet**")
        print("Status: Failed")
        print("Reason:", str(e))
        return False

def main():
    try:
        os.environ['PATH'] += r";C:\SeleniumDrivers"  # Adicionei a formatação do caminho
        driver = webdriver.Chrome()
        driver.get('http://localhost:8080/')
        
        Pass=False
        Pass=Login_User(driver)
        if(Pass):
            Pass=Test_Create_Pet(driver)    
        if(Pass):
            Pass=Test_Update_Pet(driver)
        else:
            print("Stopping Tests!") 
        if(Pass):
            Pass=Test_Delete_Pet(driver)
        else:
            print("Stopping Tests!")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()  # Feche o navegador

if __name__ == "__main__":
    main()