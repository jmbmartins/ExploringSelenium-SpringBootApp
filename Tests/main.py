from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#marcar uma data que já passou
def Login_User(driver):
    try:
        driver.get('http://localhost:8080/login')
        btn_Login = driver.find_element(By.ID, 'btnSub')
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        email_input.send_keys('jacnto@pinto.come')
        password_input.send_keys('1234')
        btn_Login.click()

        print("** Test: Login User  **")
        print("Status: Passed ")

    except Exception as e:
        print("** Test: Login User**")
        print("Status: Failed")
        print("Reason:", str(e))
        return False

def Register_Reserve(driver):
    # Teste Registro de informações de quartos.
    driver.get("http://localhost:8080/showVCNewBookingForm")
    driver.find_element(By.ID, "checkInDate")
    driver.find_element(By.ID,"checkOutDate").send_keys("12-1-2024")
    driver.find_element(By.ID, "petId").send_keys("Buddy")
    driver.find_element(By.ID, "roomTypeSelect" ).send_keys("Standard")
    driver.find_element(By.XPATH, "/html/body/form/button" ).click()

def Edit_Reservations(driver):
    try:
        driver.get("http://localhost:8080/showNewRoomForm")
        driver.find_element(By.ID, "number").send_keys("18")
        driver.find_element(By.ID, "type").send_keys("Standard")
        driver.find_element(By.ID, "price").send_keys("42069")
        driver.find_element(By.XPATH, "/html/body/div/form/button").click()

        print("Delete_All_Reservation: test passed")
    except Exception as e:
        print("Delete_All_Reservation: Test Failed")
        print("Reason:", str(e))

def Delete_Reservation(driver):
    #Elimina todas as reservas
    try:
        driver.get("http://localhost:8080/mainpageclient")
        delete_links = driver.find_elements(By.XPATH, "/html/body/div/div[4]/table/tbody/tr[2]/td[5]/a[1]")

        for delete_link in delete_links:
            delete_link.click()

        print("Delete_Reservation: Test Passed")
    except Exception as e:
        print("Delete_Reservation: Test Failed")
        print("Reason:", str(e))

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#pilha de testes
Login_User(driver)
Delete_Reservation(driver)
Edit_Reservations(driver)
Register_Reserve(driver)