from tkinter import *
from tkinter import filedialog


def select_dir():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))


def main():
    window = Tk()
    window.title("Создание накладных")
    window.geometry('332x111')

    message = StringVar()
    file_label = Label(text="Путь к файлу:")
    file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    file_path = Entry(textvariable=message)
    file_path.grid(row=0, column=1, padx=5, pady=5)
    file_btn = Button(window, text="Выбрать файл")
    file_btn.grid(column=2, row=0, padx=5, pady=5, sticky="e")

    dir_label = Label(text="Путь к папке:")
    dir_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    dir_path = Entry(textvariable=message)
    dir_path.grid(row=1, column=1, padx=5, pady=5)
    dir_btn = Button(window, text="Выбрать папку")
    dir_btn.grid(column=2, row=1, padx=5, pady=5, sticky="e")

    dir_label = Label(text="Заполните поля, нажмите кнопку."[0:35])
    dir_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    btn = Button(window, text="Начать")
    btn.grid(column=2, row=2, padx=5, pady=5, sticky="e")

    window.mainloop()


if __name__ == '__main__':
    main()
