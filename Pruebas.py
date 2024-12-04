from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configura el driver
chromedriver_path = "C:/Users/Jahaziel/Desktop/TEST/chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Navegar a la página de prueba
    driver.get("http://localhost:5038")

    # Esperar que el enlace del INTRANT esté presente
    intrant_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "INTRANT"))  # Usamos el texto del enlace como identificador
    )
    
    # Hacer clic en el enlace
    intrant_button.click()

    # Esperar la redirección (puedes esperar a que la URL cambie o que se cargue un elemento específico de la página de destino)
    WebDriverWait(driver, 15).until(
        EC.url_changes(driver.current_url)
    )

    # Verificar que la URL se haya cambiado a la esperada
    expected_url = "https://intrant.gob.do/index.php"  # Reemplaza con la URL esperada
    if driver.current_url == expected_url:
        print("Redirección exitosa a INTRANT.")
    else:
        print(f"Redirección fallida. La URL actual es {driver.current_url}")

finally:
    driver.quit()
