from AbstractClassEncryptor import AbsCodeClass
import itertools


class EncodeVigenereClass(AbsCodeClass):
    def __init__(self, text):
        super().__init__(text, 1)

    def code(self):
        KEY = input("Введите ключ(слово): ")
        len_key = len(KEY)
        cipher = ""
        for char, i in zip(self.text, itertools.cycle(range(len_key))):
            if char.isupper():
                # вычисляю численное значение для заглавной буквы
                value = (ord(char) + self.typecode*(ord(KEY[i].upper()) - self.bigstartletter)
                         - self.bigstartletter) % self.letters
                cipher += chr(value + self.bigstartletter)
            elif char.islower():
                # вычисляю численное значение для маленькой буквы
                value = (ord(char) + self.typecode*(ord(KEY[i].lower()) - self.smallstartletter)
                         - self.smallstartletter) % self.letters
                cipher += chr(value + self.smallstartletter)
            else:
                # если пробел, не учитываю
                i -= 1
                cipher += char
        print(cipher)
        return cipher


class DecodeVigenereClass(EncodeVigenereClass):
    def __init__(self, text):
        super().__init__(text)
        self.typecode = -1
