from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

#descargar el folleto de la carrera de abogacía
def folleto_utdt(url):
    #Configuramos las opciones de nuestro browser de tal manera de no "rebotar"
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Ejecutar en segundo plano (sin abrir ventana)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #Le tuve que agregar todo esto para que no me bloqueara el click de "buscar", lo bloquea igual
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # También es útil usar un User-Agent real
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    #Creamos un driver de un browser
    driver = webdriver.Chrome(options=chrome_options) # Intentar si está en PATH
    #Nos metemos en la URL
    driver.get(url)
    time.sleep(3)
    #Clickeamos para buscar propiedades
    boton_buscador=driver.find_element('xpath','//*[@id="react-filters-form"]/div/form/div/div[3]/div/div/ul/div/input')
    boton_buscador.click()
    time.sleep(3)
    #Ingresamos el barrio
    boton_buscador.send_keys("Belgrano")
    #Clickeamos buscar
    boton_buscar=driver.find_element('xpath','//*[@id="react-filters-form"]/div/form/div/div[4]/button')
    boton_buscar.click()
    time.sleep(20)
    driver.quit()
    
    #Qué pasó? Logramos nuestro cometido?

def main():
    #URL_base
    url='https://www.zonaprop.com/'
    folleto_utdt(url)
    
    
if __name__ == "__main__":
    main()       
    