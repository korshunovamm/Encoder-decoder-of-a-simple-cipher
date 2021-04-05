from abc import ABC, abstractmethod


class AbsCodeClass(ABC):
    def __init__(self, file_text, *args):
        self.text = file_text
        for i in range(len(self.text)):
            if ord(self.text[i].upper()) > ord("А") and ord(self.text[i].upper()) < ord("Я"):
                self.letters = 33
                self.smallstartletter = ord("а")
                self.bigstartletter = ord("А")
                self.typecode = args[0]
                break
            if ord(self.text[i].upper()) > ord("A") and ord(self.text[i].upper()) < ord("Z"):
                self.letters = 26
                self.smallstartletter = ord("a")
                self.bigstartletter = ord("A")
                self.typecode = args[0]
                break

    @ abstractmethod
    def code(self):
        pass
