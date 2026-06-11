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
    #Creamos un driver de un browser
    driver = webdriver.Chrome(options=chrome_options) # Intentar si está en PATH
    #Nos metemos en la URL
    driver.get(url)
    time.sleep(3)
    #Clickeamos la categoria agro
    boton_agro=driver.find_element('xpath','/html/body/div[1]/div[2]/div[2]/div/div/div[1]/a/div/div/div[2]/div')
    boton_agro.click()
    time.sleep(3)
    #Clickeamos el boton de .csv
    boton_csv=driver.find_element('xpath','//*[@id="search-results"]/div[1]/a[1]/div/div/div/div[2]/div[2]/span[1]')
    boton_csv.click()
    time.sleep(3)
    
    #clickeamos un 2do botón de descarga de .csv
    boton_descarga=driver.find_element('xpath','//*[@id="pkg-resources"]/div[1]/div/a[2]/button')
    boton_descarga.click()
    time.sleep(10)
    driver.quit()
    
    #Qué pasó? Logramos nuestro cometido?

def main():
    #URL_base
    url='https://datos.gob.ar/'
    folleto_utdt(url)
    
    
if __name__ == "__main__":
    main()       
    
    
    
