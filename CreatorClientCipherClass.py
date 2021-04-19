from Encode_and_Decode_CesarClass import EncodeCesarClass, DecodeCesarClass
from Encode_and_Decode_VigenereClass import EncodeVigenereClass, DecodeVigenereClass
from Encode_and_Decode_VernamClass import CodeVernamClass
from AutomaticHackingCesarCipher import AutomaticCesarClass


def choices(text):
    """Функция возвращает класс кодирования/декодирования Цезаря/Виженера/Вернама.
    Учитывается случай неправильного ввода данных"""

    code_class = [EncodeCesarClass, EncodeVigenereClass, CodeVernamClass,
                  DecodeCesarClass, DecodeVigenereClass, CodeVernamClass, AutomaticCesarClass]

    def except_index_error(text):
        try:
            number = int(input("""Выберите способ обработки файла:
                  зашифровать кодом Цезаря   -  0                   расшифровать кодом Цезаря   - 3
                  зашифровать кодом Виженера -  1                   расшифровать кодом Виженера - 4
                  зашифровать кодом Вернама  -  2                   расшифровать кодом Вернама  - 5
                                автоматический взлом шифра Цезаря частотным анализом - 6
                  """))
            return code_class[number](text)
        except IndexError:
            print("Неправильный номер из списка предложенных...")
            return except_index_error(text)
