import itertools


class CodeVernamClass:
    """Класс не является наследником класса AbstractClassEncryptor, так как не имеет значение,
    буквы какого языка в тексте."""

    def __init__(self, file_text):
        self.text = file_text

    def code(self):
        # KEY - ключ для шифрования Вернама - слово
        # char - один символ текста
        # i пробегает значения от 0 до длины слова KEY
        # encrypted - значение операции XOR для символа текста и соответствующкй буквы ключа
        # cipher - конечный результат гифрования - зашифрованный/расшифрованный текст
        cipher = []
        KEY = input("Введите ключ(слово): ")
        len_key = len(KEY)
        for char, i in zip(self.text, itertools.cycle(range(len_key))):
            encrypted = ord(char) ^ ord(KEY[i % len_key])
            cipher.append(chr(encrypted))
        print(''.join(cipher))
        return ''.join(cipher)
