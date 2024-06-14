import xlrd
import xlwt

route1="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones.xls"
route2="../../Big Data with Python/BigDataPython-master/data/Cap1/subvenciones_total.xls"


'''
with xlrd.open_workbook(route1) as book:
  asocs={}
  #if the book has one sheet,you could use this code book.sheet_by_index(0) or book.sheet_by_name("sheet 1")
  for sheet in book.sheets():
    for i in range(1, sheet.nrows):
      sheet_row=sheet.row(i)
      center= sheet_row[0].value
      subsidy= sheet_row[2].value
      if center in asocs:
        asocs[center]+= subsidy
      else:
        asocs[center]= subsidy
  print(asocs)


'''

with xlrd.open_workbook(route1) as book_read:
  asocs={}
  book_write= xlwt.Workbook()
  for name in book_read.sheet_names():
    sheet_read = book_read.sheet_by_name(name)
    sheet_write= book_write.add_sheet(name)
    for i in range(sheet_read.nrows):
      for j in range(sheet_read.ncols):
        cell_value= sheet_read.cell(i,j).value
        sheet_write.write(i,j, cell_value)
      if i !=0:
        sheet_row= sheet_read.row(i)
        center= sheet_row[0].value
        sub= sheet_row[2].value
        if center in asocs:
          asocs[center]+= sub
        else:
          asocs[center]= sub
  sheet_write= book_write.add_sheet('Totales')
  sheet_write.write(0,0, "Asociación")
  sheet_write.write(0,1, "Importe total")
  sheet_write.write(0,2, "Importe justificado")
  sheet_write.write(0,3, "Restante")

  for i, key in enumerate(asocs):
    sheet_row=i+1
    sheet_form=i+2

    sheet_write.write(sheet_row, 0, key)
    sheet_write.write(sheet_row, 1, asocs[key])
    sheet_write.write(sheet_row, 2, 0)

    sheet_write.write(sheet_row, 3, xlwt.Formula("C"+str(sheet_form)+"-"+"B"+str(sheet_form)))

  book_write.save(route2)