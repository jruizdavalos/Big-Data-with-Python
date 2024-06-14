import json
import csv


route1="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.json"
route2="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones_agrupadas.json"
route3="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.csv"
route4="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones_totales.json"



'''
#problem with number 1.000.000 because json does not catch value so create new json file  use csv.

with open(route1, encoding='utf-8') as fich_read, open(route2,'w',encoding='utf-8') as fich_write:
  data= json.load(fich_read)
  asoc_str="Asociación"
  act_str="Actividad Subvencionada"
  imp_str="Importe en euros"
  lista=[]
  list_act=[]
  asoc_actual=""
  dicc={}
  for element in data:
    asoc=element[asoc_str]
    act= element[act_str]
    imp= float(element[imp_str])
    if asoc_actual !=asoc:
      dicc["Actividades"]= list_act
      list_act=[]
      dicc={"Asosiación":asoc}
      lista.append(dicc)
    list_act.append({act_str:act,
                    imp_str:imp})
    asoc_actual= asoc
  print(lista)
  json.dump(lista, fich_write,ensure_ascii=False)

'''

with open(route3, encoding='latin1') as fich_read, open(route4, 'w', encoding='utf-8') as fich_write:
    dict_read = csv.DictReader(fich_read)
    asoc_str = "Asociación"
    act_str = "Actividad Subvencionada "
    imp_str = "Importe"
    lista = []
    lista_act = []
    asoc_actual = ""
    dicc = {}
    gasto = 0
    for line in dict_read:
        asoc = line[asoc_str]
        act = line[act_str]
        imp = float(line[imp_str])
        if asoc_actual != asoc:
            dicc["Actividades"] = lista_act
            dicc["Gasto"] = gasto
            dicc = {"Asociación": asoc}
            lista.append(dicc)
            lista_act = []
            gasto = 0
        lista_act.append({act_str : act, imp_str : imp})
        gasto = gasto + imp
        asoc_actual = asoc
    json.dump(lista, fich_write, ensure_ascii=False, indent=4)