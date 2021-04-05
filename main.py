from Encode_and_Decode_CesarClass import EncodeCesarClass, DecodeCesarClass
from Encode_and_Decode_VigenereClass import EncodeVigenereClass, DecodeVigenereClass
from Encode_and_Decode_VernamClass import CodeVernamClass


def choices(text):
    """Функция возвращает класс кодирования/декодирования Цезаря/Виженера/Вернама.
    Учитывается случай неправильного ввода данных"""

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


# читаю текст файла
path = input("Введите путь к файлу: ")
with open(path, encoding='utf-8', mode='r') as f:
    TEXT = f.read()
f.close()


# вывод шифрования в консоль
a = choices(TEXT).code()
# choices(a).code()
