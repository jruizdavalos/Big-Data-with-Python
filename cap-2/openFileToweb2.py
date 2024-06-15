#information is taken from a web site

import requests

#add more library
import csv
import matplotlib.pyplot as plt


url="https://www.mambiente.madrid.es/opendata/horario.txt"
path="../../Big Data with Python/BigDataPython-master/data/Cap1/"
resp=requests.get(url)
'''
#first crete to file horario.txt and then execute

with open (path+'horario.txt','wb') as output:
  output.write(resp.content)

'''

#execute file horario add librari csv and mathplotlib
'''

    if(row[0]+row[1]+row[2] =='28079004' and row[3]='12'):
      plt.title("Oxido de Nitrogeno: ", row[8]+"/"+row[7]+"/"+row[6])

'''
with open (path+'horario.txt') as csvfile:
  readCSV= csv.reader(csvfile, delimiter=',')
  for row in readCSV:
    if(row[0]+row[1]+row[2]=='28079004' and row[3]=='12'):
      plt.title("Oxido de Nitrogeno: " + row[8]+"/"+ row[7]+"/"+ row[6])
      hora=0
      desp=9
      vs=[]
      horas=[]
      while hora<=23:
        if row[desp+2*hora+1]=='V':
          vs.append(row[desp+2*hora])
          horas.append(hora)
        hora+=1
      plt.plot(horas,vs)
      plt.show()
      print("asas")