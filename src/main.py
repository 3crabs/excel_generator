import xlrd
from shutil import copyfile
import openpyxl


def read_file(file_path: str) -> list:
    read_book = xlrd.open_workbook(file_path, on_demand=True)
    sheet = read_book.sheet_by_index(0)
    return [sheet.row_values(r) for r in range(1, sheet.nrows)]


def make_invoice_file(invoice: list, template_file_path: str, save_dir_path: str):
    new_file_path = save_dir_path + "/" + invoice[1] + ".xlsx"
    copyfile(template_file_path, new_file_path)
    wb = openpyxl.load_workbook(filename=new_file_path)
    sheet = wb['list']
    sheet['O7'] = invoice[1]
    sheet['BI7'] = invoice[2]
    sheet['BD11'] = invoice[3]
    sheet['BD12'] = invoice[4]
    sheet['B17'] = invoice[5]
    sheet['BD17'] = invoice[6]
    sheet['B19'] = invoice[7]
    sheet['AJ24'] = invoice[1]
    sheet['BI24'] = invoice[2]
    sheet['BD36'] = invoice[3]
    sheet['BD37'] = invoice[4]
    sheet['B45'] = invoice[7]
    sheet['AD45'] = invoice[5]
    sheet['AM45'] = invoice[6]
    sheet['BD45'] = invoice[7]
    sheet['CF45'] = invoice[5]
    sheet['CO45'] = invoice[6]
    wb.save(new_file_path)
    print('Обработан файл №' + invoice[1])


def main():
    source_file_path = "../resources/Исходник.xlsx"
    template_file_path = "../resources/Шаблон.xlsx"
    save_dir_path = "../resources/save_dir"
    invoices = read_file(source_file_path)
    for invoice in invoices:
        make_invoice_file([""] + [str(a) for a in invoice], template_file_path, save_dir_path)


if __name__ == '__main__':
    main()
