import heapq
from AbstractClassEncryptor import AbsCodeClass


class AutomaticCesarClass(AbsCodeClass):
    def code_cesar(self, key):
        self.typecode = key
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

    def code(self):
        """Выводит ключ кода Цезаря по часто встречающейся букве"""
        count = {chr(x): 0 for x in range(self.smallstartletter, self.smallstartletter + self.letters - 1)}
        heap = []
        for char in self.text:
            if char.isalpha():
                count[char.lower()] += 1
                heapq.heappush(heap, (count[char.lower()], char.lower()))
        key_cesar_encrypt = -abs(ord(heapq.heappop(heap)[1]) - self.smallstartletter)
        self.code_cesar(key_cesar_encrypt)
