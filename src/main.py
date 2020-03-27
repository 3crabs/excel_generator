import xlrd

from src.invoice import Invoice


def read_file(file_path: str) -> list:
    read_book = xlrd.open_workbook(file_path, on_demand=True)
    sheet = read_book.sheet_by_index(0)
    return [sheet.row_values(r) for r in range(1, sheet.nrows)]


def convert(rows_list: list) -> list:
    return [Invoice(row) for row in rows_list]


def copy(file_path1: str, file_path2: str):
    print(file_path1)
    print(file_path2)


if __name__ == '__main__':
    source_filepath = "../resources/Исходник.xlsx"
    rows = convert(read_file(source_filepath))
