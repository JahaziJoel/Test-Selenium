import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()

driver.get("http://localhost:5038")  
try:
    def localizar_y_hacer_click_registro():
        for intento in range(3):  
            try:
                registro_boton = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Registro')]"))
                )
                registro_boton.click()
                time.sleep(2)  
                return  
            except StaleElementReferenceException:
                print(f"Intento {intento + 1}: El elemento no es válido. Reintentando...")
                time.sleep(2)  

        raise Exception("No se pudo hacer clic en el botón 'Registro' después de varios intentos.")

    localizar_y_hacer_click_registro()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Registro')]"))
    )
    time.sleep(2) 
    def localizar_y_hacer_click_nuevo_registro():
        for intento in range(3):  
            try:
                nuevo_registro_boton = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Nuevo Registro')]"))
                )
                nuevo_registro_boton.click()
                time.sleep(2)  
                return  
            except StaleElementReferenceException:
                print(f"Intento {intento + 1}: El elemento no es válido. Reintentando...")
                time.sleep(2)  

        raise Exception("No se pudo hacer clic en el botón 'Nuevo Registro' después de varios intentos.")

    localizar_y_hacer_click_nuevo_registro()

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Nuevo Registro')]"))
    )
    time.sleep(2)  
    driver.save_screenshot("captura_after_nuevo_registro.png")

except Exception as e:
    print(f"Error: {e}")
    driver.save_screenshot("captura_error.png")  
driver.quit()
