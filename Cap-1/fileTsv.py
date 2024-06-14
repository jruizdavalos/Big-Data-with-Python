#case 1

import csv

route1="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.csv"
route2="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.tsv"

with open(route1, encoding="latin1") as file_read, open(route2,'w',encoding="latin1") as file_write:
  dict_reader= csv.DictReader(file_read)
  campos= dict_reader.fieldnames
  writer= csv.DictWriter(file_write,delimiter='\t', fieldnames=campos)
  writer.writeheader()
  for line in dict_reader:
    writer.writerow(line)

with open(route2, encoding='latin1') as file:
  dict_reader= csv.DictReader(file,delimiter='\t')
  asocs={}
  for line in dict_reader:
    center= line['Asociación']
    subsidy=float(line['Importe'])
    if center in asocs: 
      asocs[center]+=subsidy
    else:
      asocs[center]= subsidy
  print(f"dict: {asocs}")