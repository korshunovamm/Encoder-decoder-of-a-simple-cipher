from AbstractClassEncryptor import AbsCodeClass


class EncodeCesarClass(AbsCodeClass):
    """Super().__init__() инициализирует переменную typecode, которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение со знаком '+' в случае кодирования,
    со знаком '-' в случае декодирования. Далее используется функция кодирования текста."""

    def __init__(self, text):
        def except_value_error():
            try:
                key_cesar = int(input("Введите ключ(число): "))
                return key_cesar
            except ValueError:
                print("Это не число(((")
                except_value_error()
        super().__init__(text, except_value_error())

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
        print(cipher)
        return cipher


class DecodeCesarClass(EncodeCesarClass):
    """Super().__init__() инициализирует переменную typecode, которая является ключом к шифру Цезаря,
    поданного на вход через консоль. Typecode принимает значение со знаком '+' в сдучае кодирования,
    со знаком '-' в случае декодирования. Далее используется функция кодирования текста, которая
    наследуется, как материнская."""

    def __init__(self, text):
        super().__init__(text)
        self.typecode = -self.typecode
