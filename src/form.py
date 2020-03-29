from tkinter import *
from tkinter import filedialog as fd

window = Tk()
file_path = StringVar()
dir_path = StringVar()
button = None


def check_button_state():
    global button
    button["state"] = NORMAL
    if file_path is None:
        button["state"] = DISABLED
    if dir_path is None:
        button["state"] = DISABLED


def select_dir():
    global dir_path
    dir_name = fd.askdirectory(title='Выберите папку для сохранения результатов')
    dir_path.set(dir_name)
    check_button_state()


def select_file():
    global file_path
    file_name = fd.askopenfile(title='Выберите файл данных', filetypes=[('xlsx files', ['.xlsx'])])
    file_path.set(file_name.name)
    check_button_state()


def start():
    print('start')


def main():
    global window
    global file_path
    global dir_path
    global button

    window.title("Создание накладных")
    window.geometry('332x111')

    file_label = Label(text="Путь к файлу:")
    file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    file_input = Entry(textvariable=file_path)
    file_input.grid(row=0, column=1, padx=5, pady=5)
    file_button = Button(window, text="Выбрать файл", command=select_file)
    file_button.grid(column=2, row=0, padx=5, pady=5, sticky="e")

    dir_label = Label(text="Путь к папке:")
    dir_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    dir_input = Entry(textvariable=dir_path)
    dir_input.grid(row=1, column=1, padx=5, pady=5)
    dir_button = Button(window, text="Выбрать папку", command=select_dir)
    dir_button.grid(column=2, row=1, padx=5, pady=5, sticky="e")

    dir_label = Label(text="Заполните поля, нажмите кнопку."[0:35])
    dir_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    button = Button(window, text="Начать", command=start)
    button.grid(column=2, row=2, padx=5, pady=5, sticky="e")
    button["state"] = DISABLED

    window.mainloop()


if __name__ == '__main__':
    main()
