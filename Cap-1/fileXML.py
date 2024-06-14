import xml.etree.ElementTree as ET
route1="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.xml"
route2="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones_gasto.xml"
'''
#case 1 read xml file

tree= ET.parse(route1)
raiz= tree.getroot()
asocs={}
for fila in raiz:
  centro = fila[0].text
  subvencion= float(fila[2].text)
  if centro in asocs:
    asocs[centro]+=subvencion
  else:
    asocs[centro]=subvencion
print(asocs)
'''
#case 2
tree= ET.parse(route1)
raiz = tree.getroot()
new_tree= ET.ElementTree()
new_raiz= ET.Element("Raiz")
new_tree._setroot(new_raiz)
elemnt_actual= ET.Element("Asociacion")
asoc_actual=""
actividades= ET.SubElement(elemnt_actual,"Actividades")
gasto=0
for fila in raiz.findall('Row'):
  asoc=fila.find('Asociaci_n').text
  act= fila.find('Actividad_Subvencionada').text
  imp= float(fila.find('Importe').text)
  if asoc_actual !=asoc:
    gas_total= ET.SubElement(elemnt_actual,"Total")
    gas_total.text=str(gasto)
    elemnt_actual=ET.SubElement(new_raiz,"Asociacion")
    elemnt_actual.set('nombre',asoc)
    actividades= ET.SubElement(elemnt_actual,"Actividades")
    gasto=0
  act_element=ET.SubElement(actividades,"Actividad")
  nom_element= ET.SubElement(act_element,"Nombre")
  nom_element=act
  imp_element=ET.SubElement(act_element,"Subvencion")
  imp_element.text= str(imp)
  gasto+=imp
  asoc_actual= asoc

new_tree.write(route2)
