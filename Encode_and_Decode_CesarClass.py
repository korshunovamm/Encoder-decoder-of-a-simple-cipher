from tkinter import Label, Button, Entry, END, messagebox
from AbstractClassEncryptor import AbsCodeClass


class EncodeCesarClass(AbsCodeClass):
    """Super().__init__() инициализирует переменную typecode,
    которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает
    значение со знаком '+' в случае кодирования,
    со знаком '-' в случае декодирования.
    Далее используется функция кодирования текста."""

    def __init__(self, text, window, bg_color):
        """
        для работы в консоли:
        def except_value_error():
            try:
                key_cesar = int(input("Введите ключ(число): "))
                self.typecode = key_cesar
            except ValueError:
                print("Это не число(((")
                except_value_error()
        """
        def clicked():
            key_cesar = txt.get()
            if not key_cesar.isdigit() or key_cesar == '¯|_(ツ)_|¯':
                messagebox.showinfo(':(((((', 'Это не число')
                txt.delete(0, END)
                txt.insert(0, '¯|_(ツ)_|¯')
            else:
                self.typecode = int(key_cesar)
                code_text = self.code()
                lbl_code_text = Label(text=code_text)
                lbl_code_text.pack()

        lbl_key = Label(text="Введите ключ(число): ", bg=bg_color)
        lbl_key.pack()
        txt = Entry(window, width=20, bg=bg_color)
        txt.pack()
        ready = Button(window, text="Готово!", command=clicked, bg=bg_color)
        ready.pack()

        super().__init__(text, window)

    def code(self):
        """
        self.typecode - ключ для шифрования(принимается с консоли)-число
        cipher - конечный результат гифрования -
        зашифрованный/расшифрованный текст
        char - один символ текста
        self.letters - количество букв в алфавите
        self.bigstartletter/self.smallstartletter - номер
        первой заглавной/маленькой буквы в алфавите
        """
        if self.typecode is not None:
            return self.parsing_cesar()


class DecodeCesarClass(EncodeCesarClass):
    """Super().__init__() инициализирует переменную typecode,
    которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение
    со знаком '+' в сдучае кодирования,
    со знаком '-' в случае декодирования. Далее используется
    функция кодирования текста, которая
    наследуется, как материнская."""

    def __init__(self, text, window, bg_color):
        super().__init__(text, window, bg_color)
        if self.typecode is not None:
            self.typecode = -self.typecode
