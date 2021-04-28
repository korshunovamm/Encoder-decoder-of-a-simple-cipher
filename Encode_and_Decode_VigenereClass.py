from tkinter import Label, Entry, Button, END
from tkinter import messagebox
from AbstractClassEncryptor import AbsCodeClass
import itertools


class EncodeVigenereClass(AbsCodeClass):
    """Super().__init__() инициализирует переменную typecode, которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение '+1' в случае кодирования,
    '-1' в случае декодирования. Далее используется функция кодирования текста."""

    def __init__(self, text, window, bg_color):
        super().__init__(text, window, bg_color)
        self.typecode = 1
        self.bg_color = bg_color
        self.code_vig = None

        def clicked():
            key_vigener = txt.get()
            if not key_vigener.isalpha() or key_vigener == '¯|_(ツ)_|¯':
                messagebox.showinfo(':(((((', 'Это не слово')
                txt.delete(0, END)
                txt.insert(0, '¯|_(ツ)_|¯')
            else:
                self.code_vig = key_vigener
                code_text = self.code()
                lbl_code_text = Label(text=code_text)
                lbl_code_text.pack()

        lbl_key = Label(text="Введите ключ(слово): ", bg=self.bg_color)
        lbl_key.pack()
        txt = Entry(self.window, width=20, bg=self.bg_color)
        txt.pack()
        ready = Button(self.window, text="Готово!", command=clicked, bg=self.bg_color)
        ready.pack()

    def code(self):
        """
        self.typecode: =1 при кодировании, =-1 при декодировании
        key_vig - ключ для шифрования Виженером - слово
        cipher - конечный результат гифрования - зашифрованный/расшифрованный текст
        char - один символ текста
        self.letters - количество букв в алфавите
        self.bigstartletter/self.smallstartletter - номер первой заглавной/маленькой буквы в алфавите
        i пробегает значения от 0 до длины слова key_vig
        """
        """
        для работы в консоли:
        def except_value_error():
            while True:
                key_vigener = input("Введите ключ(слово): ")
                if not key_vigener.isalpha():
                    print("Это не слово(((")
                else:
                    break
            self.code_vig = key_vigener

        except_value_error()
        """
        if self.code_vig is not None:
            len_key = len(self.code_vig)
            cipher = ""
            for char, i in zip(self.text, itertools.cycle(range(len_key))):
                if char.isupper():
                    # вычисляю численное значение для заглавной буквы
                    value = (ord(char) + self.typecode*(ord(self.code_vig[i].upper()) - self.bigstartletter) -
                             self.bigstartletter) % self.letters
                    cipher += chr(value + self.bigstartletter)
                elif char.islower():
                    # вычисляю численное значение для маленькой буквы
                    value = (ord(char) + self.typecode*(ord(self.code_vig[i].lower()) - self.smallstartletter) -
                             self.smallstartletter) % self.letters
                    cipher += chr(value + self.smallstartletter)
                else:
                    # если пробел, не учитываю
                    i -= 1
                    cipher += char
            return cipher


class DecodeVigenereClass(EncodeVigenereClass):
    """Super().__init__() инициализирует переменную typecode, которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение '+1' в случае кодирования,
    '-1' в случае декодирования. Далее используется функция кодирования текста, которая
    наследуется, как материнская."""

    def __init__(self, text, window, bg_color):
        super().__init__(text, window, bg_color)
        self.typecode = -1
