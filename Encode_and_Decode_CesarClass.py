from AbstractClassEncryptor import AbsCodeClass


class EncodeCesarClass(AbsCodeClass):
    def __init__(self, text):
        super().__init__(text, int(input("Введите ключ(число): ")))

    def code(self):
        cipher = ''
        for char in self.text:
            if char.isupper():
                cipher += chr((ord(char) + self.typecode - self.bigstartletter) % self.letters
                              + self.bigstartletter)
            elif char.islower():
                cipher += chr((ord(char) + self.typecode - self.smallstartletter) % self.letters
                              + self.smallstartletter)
            else:
                cipher += char
        print(cipher)
        return cipher


class DecodeCesarClass(EncodeCesarClass):
    def __init__(self, text):
        super().__init__(text)
        self.typecode = -self.typecode
