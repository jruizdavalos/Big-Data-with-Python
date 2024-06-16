#use of beatufulsoup

#import library
from bs4 import BeautifulSoup
#i create project in html

url=r"../../Big Data with Python/big-Data/cap-2/mini.html"

with open(url,"r") as f:
  page=f.read()
soup=BeautifulSoup(page,"html.parser")

print(soup.prettify())

childrenDoc= list(soup.children)
print("Children  --",childrenDoc)
print([type(item) for item in childrenDoc])

html=childrenDoc[2]
print(list(html.children))

body= list(html.children)[3]
print(list(body.children))

divDate= list(body.children)[1]
print(divDate)
print(list(divDate))
print(list(divDate.children))
print(divDate.get_text())

#relative navegation
divs= soup.find_all("div")
#i want to show the element of first div
print(divs[0].get_text())
