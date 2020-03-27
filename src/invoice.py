class Invoice:
    def __init__(self, items):
        self.number = items[0]  # номер накладной
        self.date = items[1]  # дата и время
        self.shot_name = items[2]  # краткое наименование
        self.location = items[3]  # адресс
        self.count_packages = items[4]  # количество мест
        self.count_scattering = items[5]  # количество россыпью
        self.weight = items[6]  # вес брутто
