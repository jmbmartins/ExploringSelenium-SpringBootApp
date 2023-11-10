from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


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


def register_new_room(driver):
    try:
        # Teste Registro de informações de quartos.
        driver.get("http://localhost:8080/showNewRoomForm")
        # numero do novo quarto
        driver.find_element(By.ID, "number").send_keys("69")
        # tipo the quarto
        driver.find_element(By.ID, "type").send_keys("Deluxe")
        # preco do mesmo
        driver.find_element(By.ID, "price").send_keys("420")

        driver.find_element(By.XPATH, "/html/body/div/form/button").click()

        print("register_new_room: test passed")
    except Exception as e:
        print("register_new_room: Test Failed")
        print("Reason:", str(e))


def edit_room(driver):
    try:
        # Teste Registro de informações de quartos.
        driver.get("http://localhost:8080/showNewRoomForm")
        # numero do novo quarto
        driver.find_element(By.ID, "number").send_keys("69")
        # tipo the quarto
        driver.find_element(By.ID, "type").send_keys("Deluxe")
        # preco do mesmo
        driver.find_element(By.ID, "price").send_keys("420")

        driver.find_element(By.XPATH, "/html/body/div/form/button").click()

        print("edit_room: test passed")
    except Exception as e:
        print("edit_room: Test Failed")
        print("Reason:", str(e))


def delete_room(driver):
    # Elimina todas as reservas
    try:
        driver.get("http://localhost:8080/mainpageclient")
        delete_links = driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[4]/a[2]")

        for delete_link in delete_links:
            delete_link.click()

        print("Delete_Reservation: Test Passed")
    except Exception as e:
        print("Delete_Reservation: Test Failed")
        print("Reason:", str(e))


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# pilha de testes
Login_User(driver)
register_new_room(driver)
delete_room(driver)
edit_room(driver)
