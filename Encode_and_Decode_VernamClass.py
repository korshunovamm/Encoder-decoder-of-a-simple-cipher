from tkinter import Label, Button, Entry, END, messagebox
import itertools


class CodeVernamClass():
    """Класс не является наследником класса AbstractClassEncryptor, так как не имеет значение,
    буквы какого языка в тексте."""

    def __init__(self, text, window=None, bg_color=None):
        self.text = text
        self.window = window
        self.bg_color = bg_color
        self.typecode = None

        def clicked():
            key_cesar = txt.get()
            if not key_cesar.isalpha() or key_cesar == '¯\_(ツ)_/¯':
                messagebox.showinfo(':(((((', 'Это не слово')
                txt.delete(0, END)
                txt.insert(0, '¯\_(ツ)_/¯')
            else:
                self.typecode = key_cesar
                code_text = self.code()
                lbl_code_text = Label(text=code_text)
                lbl_code_text.pack()

        lbl_key = Label(text="Введите ключ(слово): ", bg=bg_color)
        lbl_key.pack()
        txt = Entry(window, width=20, bg=bg_color)
        txt.pack()
        ready = Button(window, text="Готово!", command=clicked, bg=bg_color)
        ready.pack()

        # super().__init__(text, window, )

    def code(self):
        """
        KEY - ключ для шифрования Вернама - слово
        char - один символ текста
        i пробегает значения от 0 до длины слова KEY
        encrypted - значение операции XOR для символа текста и соответствующкй буквы ключа
        cipher - конечный результат гифрования - зашифрованный/расшифрованный текст
        """

        """ 
        для работы в консоли:
        def except_value_error():
            while True:
                key_vernam = input("Введите ключ(слово): ")
                if not key_vernam.isalpha():
                    print("Это не слово(((")
                else:
                    break
            self.typecode = key_vernam
        """
        if self.typecode != None:
            cipher = []
            len_key = len(self.typecode)
            for char, i in zip(self.text, itertools.cycle(range(len_key))):
                encrypted = ord(char) ^ ord(self.typecode[i % len_key])
                cipher.append(chr(encrypted))
            return ''.join(cipher)
