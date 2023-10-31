import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://localhost:8080/')


def register_client():
    # Test 1: Create a New Client
    try:
        # Voltar para a página de login
        driver.get('http://localhost:8080/')

        # Encontrar o botão de registo
        btnRegister = driver.find_element(By.ID, 'btnregister')
        btnRegister.click()

        # Esperar pela página de destino após o login (você pode adicionar uma espera explícita)
        driver.implicitly_wait(10)

        # Preencher e enviar o formulário de login com credenciais de cliente
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.ID, 'btnSub')

        email_input.send_keys('user3@example.com')
        password_input.send_keys('password3')
        login_button.click()

        # Esperar por 2 segundos
        time.sleep(2)

        # Esperar pela página de destino após o login (você pode adicionar uma espera explícita)
        driver.implicitly_wait(10)

        # Verificar o texto no elemento com id "pagetitle"
        pagetitle_element = driver.find_element(By.ID, 'pagetitle')
        text = pagetitle_element.text

        # Verificar se o texto está correto
        assert "Welcome to Pet's Hotel," in text

        print("Teste de registo do cliente foi bem-sucedido!")
    except Exception as e:
        print("Teste de registo do cliente falhou:", str(e))


'''
# Step 2: Register a new customer
def register_new_customer():
    driver.get("http://yourwebsite.com/homepage")  # Navigate to the homepage
    new_client_link = driver.find_element_by_link_text("Add Pet")
    new_client_link.click()

    name_input = driver.find_element_by_name("name")
    address_input = driver.find_element_by_name("address")
    phone_input = driver.find_element_by_name("phone")
    insert_button = driver.find_element_by_xpath("//button[@type='submit']")

    name_input.send_keys("New Customer Name")
    address_input.send_keys("123 Main St")
    phone_input.send_keys("123-456-7890")
    insert_button.click()


# Step 3: View customer information
def view_customer_information():
    driver.get("http://yourwebsite.com/homepage")  # Navigate to the homepage
    customer_info_link = driver.find_element_by_link_text("Change Information")
    customer_info_link.click()


# Step 4: Update customer details
def update_customer_details():
    driver.get("http://yourwebsite.com/homepage")  # Navigate to the homepage
    update_link = driver.find_element_by_link_text("Update")
    update_link.click()

    name_input = driver.find_element_by_name("name")
    address_input = driver.find_element_by_name("address")
    phone_input = driver.find_element_by_name("phone")
    update_button = driver.find_element_by_xpath("//button[@type='submit']")

    name_input.clear()
    name_input.send_keys("Updated Name")
    address_input.clear()
    address_input.send_keys("456 New St")
    phone_input.clear()
    phone_input.send_keys("987-654-3210")
    update_button.click()


# Step 5: Delete customer
def delete_customer():
    driver.get("http://yourwebsite.com/homepage")  # Navigate to the homepage
    delete_link = driver.find_element_by_link_text("Delete")
    delete_link.click()
    # You may need to confirm the deletion through a confirmation dialog
'''

# Main test scenario
try:
    register_client()
    # register_new_customer()
    # view_customer_information()
    # update_customer_details()
    # delete_customer()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()  # Close the browser
