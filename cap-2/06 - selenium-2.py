from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import chromedriver_autoinstaller

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

url = 'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx'
driver.get(url)
#driver.implicitly_wait(0.5)
try:
    cookies = driver.find_element(by=By.XPATH,
    value='/html/body/div[2]/div/a[2]')
    cookies.click()
    print("Cookies aceptadas.")
except Exception as e:
    print(f"No se encontró el botón de aceptar cookies o ocurrió un error: -> {e}")