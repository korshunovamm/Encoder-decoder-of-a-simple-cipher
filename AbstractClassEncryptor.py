from abc import ABC, abstractmethod


class AbsCodeClass(ABC):
    """Класс инициализируется текстом, полученным из файла, поданного на вход.
    Происходит проверка на язык(русский/английский) и устанавливается значение количества букв в алфавите,
    номер маленькой и заглавной первой буквы в алфавите по ASCII таблице. Также на вход в аргументах
    *args может быть подан typecod, который взависимости от кодирования или декодирования принимает
    противоположные по знаку значения (сделано это для того, чтобы избежать копирования кода)"""

    def __init__(self, file_text, typecode=None):
        self.text = file_text
        for i in range(len(self.text)):
            # проверка на русский алфавит
            if ord(self.text[i].upper()) > ord("А") and ord(self.text[i].upper()) < ord("Я"):
                self.letters = 32
                self.smallstartletter = ord("а")
                self.bigstartletter = ord("А")
                # самая часто втречаюшаяся буква в тексте
                self.frequency_char = ord("о")
                self.typecode = typecode
                break
            # проверка на нглийский алфавит
            if ord(self.text[i].upper()) > ord("A") and ord(self.text[i].upper()) < ord("Z"):
                self.letters = 25
                self.smallstartletter = ord("a")
                self.bigstartletter = ord("A")
                # самая часто втречаюшаяся буква в тексте
                self.frequency_char = ord("e")
                self.typecode = typecode
                break

    @ abstractmethod
    def code(self):
        pass
