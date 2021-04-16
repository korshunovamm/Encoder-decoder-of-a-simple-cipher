from tkinter import *
from tkinter import messagebox
from AbstractClassEncryptor import AbsCodeClass


class EncodeCesarClass(AbsCodeClass):
    """Super().__init__() инициализирует переменную typecode, которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение со знаком '+' в случае кодирования,
    со знаком '-' в случае декодирования. Далее используется функция кодирования текста."""

    def __init__(self, text, window):
        def except_value_error():
            try:
                key_cesar = int(input("Введите ключ(число): "))
                return key_cesar
            except ValueError:
                print("Это не число(((")
                except_value_error()

        def get_key_gui():
            key = None

            def clicked():
                while True:
                    key_cesar = txt.get()
                    if not key_cesar.isdigit():
                        messagebox.showinfo(':(((((', 'Это не число')
                        txt.delete(0, END)
                        txt.insert(0, '0')
                    else:
                        nonlocal key
                        key = key_cesar
                        return key_cesar

            lbl_key = Label(text="Введите ключ(число): ")
            lbl_key.grid(column=0, row=12)
            txt = Entry(window, width=10)
            txt.grid(column=1, row=12)
            ready = Button(window, text="Готово!", command=clicked)
            ready.grid(column=2, row=12)

            if key != None:
                return key
        super().__init__(text, window, get_key_gui())

    def code(self):
        cipher = ''
        # self.typecode - ключ для шифрования(принимается с консоли) - число
        # cipher - конечный результат гифрования - зашифрованный/расшифрованный текст
        # char - один символ текста
        # self.letters - количество букв в алфавите
        # self.bigstartletter/self.smallstartletter - номер первой заглавной/маленькой буквы в алфавите
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
        # print(cipher)
        return cipher


class DecodeCesarClass(EncodeCesarClass):
    """Super().__init__() инициализирует переменную typecode, которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение со знаком '+' в сдучае кодирования,
    со знаком '-' в случае декодирования. Далее используется функция кодирования текста, которая
    наследуется, как материнская."""

    def __init__(self, text, window):
        super().__init__(text, window)
        self.typecode = -self.typecode
