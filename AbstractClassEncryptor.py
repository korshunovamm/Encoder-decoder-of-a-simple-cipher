import sys
from abc import ABC, abstractmethod
from tkinter import messagebox


class AbsCodeClass(ABC):
    """Класс инициализируется текстом, полученным из файла, поданного на вход.
    Происходит проверка на язык(русский/английский) и устанавливается значение количества букв в алфавите,
    номер маленькой и заглавной первой буквы в алфавите по ASCII таблице. Также на вход в аргументах
    *args может быть подан typecod, который взависимости от кодирования или декодирования принимает
    противоположные по знаку значения (сделано это для того, чтобы избежать копирования кода)"""

    def __init__(self, file_text, window=None, typecode=None):
        self.text = file_text
        # ключ для шифрования
        self.typecode = typecode
        # дополнительные данные для графического интерфейса
        self.window = window
        self.letters = None
        for i in range(len(self.text)):
            """
            проверка на русский алфавит
            "А" - первая заглавная буква в русском алфавите
            "а" - первая маленькая буква в русском алфавите
            "Я" - последняя заглавная буква в русском алфавите
            self.frequency_char -самая часто втречаюшаяся буква в тексте
            """
            if ord("А") <= ord(self.text[i].upper()) <= ord("Я"):
                self.letters = 32
                self.smallstartletter = ord("а")
                self.bigstartletter = ord("А")
                self.frequency_char = ord("о")
                break
            """
            проверка на нглийский алфавит
            "А" - первая заглавная буква в английском алфавите
            "а" - первая маленькая буква в английском алфавите
            "Z" - последняя заглавная буква в английском алфавите
            """
            if ord("A") <= ord(self.text[i].upper()) <= ord("Z"):
                self.letters = 25
                self.smallstartletter = ord("a")
                self.bigstartletter = ord("A")
                self.frequency_char = ord("e")
                break
        # если в тексте нет букв латинского или руссского алфавита, то предупреждение
        if self.letters is None:
            messagebox.showinfo("В следующий раз повезёт", "В тексте должны быть буквы русского/латинского алфавита")
            sys.exit()

    def parsing_cesar(self):
        cipher = ""
        for char in self.text:
            # если буква заглавная, то и после кодирования она останется заглавной
            if char.isupper():
                cipher += chr((ord(char) + self.typecode - self.bigstartletter) % self.letters
                              + self.bigstartletter)
            # если буква заглавная, то и после кодирования она останется заглавной
            elif char.islower():
                cipher += chr((ord(char) + self.typecode - self.smallstartletter) % self.letters
                              + self.smallstartletter)
            # если символ то он сохраняется, не внося никакой вклад в шифрование
            else:
                cipher += char
        return cipher

    @abstractmethod
    def code(self):
        pass
