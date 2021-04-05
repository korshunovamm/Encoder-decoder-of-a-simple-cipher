import itertools


class CodeVernamClass:
    def __init__(self, file_text):
        self.text = file_text

    def code(self):
        cipher = []
        KEY = input("Введите ключ(слово): ")
        len_key = len(KEY)
        for char, i in zip(self.text, itertools.cycle(range(len_key))):
            encrypted = ord(char) ^ ord(KEY[i % len_key])
            cipher.append(chr(encrypted))
        print(''.join(cipher))
        return ''.join(cipher)
