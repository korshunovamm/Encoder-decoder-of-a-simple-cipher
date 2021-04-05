from Encode_and_Decode_CesarClass import EncodeCesarClass, DecodeCesarClass
from Encode_and_Decode_VigenereClass import EncodeVigenereClass, DecodeVigenereClass
from Encode_and_Decode_VernamClass import CodeVernamClass


def choices(text):
    code_class = [EncodeCesarClass, EncodeVigenereClass, CodeVernamClass,
                  DecodeCesarClass, DecodeVigenereClass, CodeVernamClass]

    def excepterror(text):
        try:
            number = int(input("""Выберите способ обработки файла:
                  зашифровать кодом Цезаря   -  0                   расшифровать кодом Цезаря   - 3
                  зашифровать кодом Виженера -  1                   расшифровать кодом Виженера - 4
                  зашифровать кодом Вернама  -  2                   расшифровать кодом Вернама  - 5
                  """))
            return code_class[number](text)
        except IndexError:
            excepterror(text)
    return excepterror(text)


path = input("Введите путь к файлу: ")
with open(path, encoding='utf-8', mode='r') as f:
    TEXT = f.read()
f.close()


a = choices(TEXT).code()
choices(a).code()
