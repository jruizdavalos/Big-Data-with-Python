#information is taken from a web site

import requests

#add more library
import csv
import matplotlib.pyplot as plt
# directly read the file in format utf-8
import codecs
#reed get of request.get()
from contextlib import closing



url="https://www.mambiente.madrid.es/opendata/horario.txt"
path="../../Big Data with Python/BigDataPython-master/data/Cap1/"


with closing(requests.get(url, stream=True)) as r:
  reader= csv.reader(codecs.iterdecode(
                      r.iter_lines(),
                      'utf-8'),
                      delimiter=',')
  for row in reader:
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
