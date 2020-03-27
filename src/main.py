import xlrd


if __name__ == '__main__':

    source_filename = "../resources/Исходник.xlsx"
    read_book = xlrd.open_workbook(source_filename, on_demand=True)

    sheet = read_book.sheet_by_index(0)  # Читаем из первого листа
    val = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    for elem in val[1:]:
        print(elem)
