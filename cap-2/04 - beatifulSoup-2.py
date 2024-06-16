import requests
from bs4 import BeautifulSoup



url=r"https://www.boe.es/informacion/hora_oficial.php"

r=requests.get(url)
print(r)

soup=BeautifulSoup(r.content,"html.parser")
hora_oficial=soup.find("div",id='hora-oficial')
print(list(hora_oficial.children)[1].get_text())