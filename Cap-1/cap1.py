
import csv

route1="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.csv"
route2="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones_esc.csv"

'''
# case 1


with open(route1, encoding="latin1") as file_csv:
  read=csv.reader(file_csv)
  next(read, None) #omit title
  price_total=0
  for x in read:
    price_str=x[2]
    price = float(price_str)
    price_total+=price
  print(price_total)

  
#case 2

with open(route1, encoding="latin1")as file_csv:
  dict_read= csv.DictReader(file_csv)# omit title automatic for use DictReader
  asocs={}
  for line in dict_read:
    center= line['Asociación']
    subsidy=float(line['Importe'])
    if center in asocs: 
      asocs[center]+=subsidy
    else:
      asocs[center]= subsidy
  print(f"dict: {asocs}")

#Case 3

with open(route1, encoding="latin1")as file_csv:
  dict_read= csv.DictReader(file_csv,fieldnames=['Asociación','Actividad Subvencionada','Importe'])# omit title automatic for use DictReader
  asocs={}
  for line in dict_read:
    center= line['Asociación']
    subsidy=float(line['Importe'])
    if center in asocs: 
      asocs[center]+=subsidy
    else:
      asocs[center]= subsidy
  print(f"dict: {asocs}")

'''
with open(route1,encoding='latin1') as file_read, open(route2,'w',encoding='latin1') as file_writer:
  dict_reader= csv.DictReader(file_read)
  campos= dict_reader.fieldnames + ['Justificación Requerida','Justificación Recibida']
  writer= csv.DictWriter(file_writer, fieldnames=campos)
  writer.writeheader()
  for line in dict_reader:
    if float(line['Importe'])>300:
      line['Justificación Requerida']="Sí"
    else:
      line['Justificación Requerida']="NO"
    line['Justificación Recibida']="NO"
    writer.writerow(line)


with open(route2,'r',encoding='latin1') as file:
  reader=csv.DictReader(file)
  for line in reader:
    print("asdasssss",line)



