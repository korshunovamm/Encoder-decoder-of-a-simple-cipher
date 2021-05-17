from AbstractClassEncryptor import AbsCodeClass


class AutomaticCesarClass(AbsCodeClass):
    def __init__(self, text, window, bg_color):
        super().__init__(text, window, bg_color)

    def code_cesar(self, key):
        """
        self.typecode - ключ для шифрования(принимается с консоли) - число
        cipher - конечный результат шифрования - зашифрованный/расшифрованный
        текст
        char - один символ текста
        self.letters - количество букв в алфавите
        self.bigstartletter/self.smallstartletter - номер первой
        заглавной/маленькой буквы в алфавите
        """
        self.typecode = key
        return self.parsing_cesar()

    def code(self):
        """Выводит ключ кода Цезаря по часто встречающейся букве."""
        count = {chr(x): 0 for x in
                 range(self.smallstartletter,
                       self.smallstartletter + self.letters)}
        max_count = 0
        max_char = None
        for char in self.text:
            if char.isalpha():
                count[char.lower()] += 1
                max_count = count[char.lower()] if \
                    count[char.lower()] >= max_count else max_count
                max_char = char.lower() \
                    if count[char.lower()] >= max_count else max_char
        key_cesar_encrypt = -abs(ord(max_char) - self.frequency_char)
        return self.code_cesar(key_cesar_encrypt)
