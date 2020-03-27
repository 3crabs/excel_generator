import xlwt, xlrd
from xlutils.copy import copy as xlcopy

source_filename = "example.xlx"
destination_filename = "example_new.xls"

read_book = xlrd.open_workbook(source_filename, on_demand=True)

read_sheet = read_book.get_sheet(0)  # Читаем из первого листа
write_book = xlcopy(read_book)  # Копируем таблицу в память, в неё мы ниже будем записывать
write_sheet = write_book.get_sheet(0)  # Будем записывать в первый лист
write_sheet.write(0, 0, read_sheet.cell_value(0, 0) + 42)  # Прибавим к значению из ячейки "A1" число 42
write_book.save(destination_filename)