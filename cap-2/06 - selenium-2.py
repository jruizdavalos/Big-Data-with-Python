from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

url = 'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx'
driver.get(url)
driver.implicitly_wait(1)
try:
    cookies = driver.find_element(by=By.XPATH,
    value='/html/body/div[2]/div/a[2]')
    cookies.click()
    print("Cookies aceptadas.")
except Exception as e:
    print(f"No se encontró el botón de aceptar cookies o ocurrió un error: -> {e}")

driver.implicitly_wait(1)
coord=driver.find_element(By.LINK_TEXT,"COORDENADAS")
coord.click()

lat=driver.find_element(By.ID,"ctl00_Contenido_txtLatitud")
lon=driver.find_element(By.ID,"ctl00_Contenido_txtLongitud")
latitud  = "28.2723368"
longitud = "-16.6600606"


lat.send_keys(latitud)
lon.send_keys(longitud)

datos = driver.find_element(By.NAME, "ctl00$Contenido$btnDatos")
datos.click()
html=driver.find_element(By.XPATH,"/html")
print(html.text)

head = driver.find_element(By.XPATH,"/html/head")
body = driver.find_element(By.XPATH,"/html/body")
html2 = body.find_element(By.XPATH,"/html")
hijos = driver.find_elements(By.XPATH,"/html/body/*")
for element in hijos:
    print(element.tag_name)

#divs=driver.find_element(By.XPATH("/hmtl/body/*/div"))
divs = driver.find_elements(By.XPATH,"/html/body//div")
print(f"divs: {len(divs)}")

labels = driver.find_elements(By.XPATH,"//label")
print(len(labels))

#filter

xpath = "//*[./span/text()='Referencia catastral']//label"
etiqs = driver.find_element(By.XPATH,xpath)
print(etiqs.text)
xpath = "//*[./span/text()='Uso principal']//label"
etiqs = driver.find_element(By.XPATH,xpath)
print(etiqs.text)

