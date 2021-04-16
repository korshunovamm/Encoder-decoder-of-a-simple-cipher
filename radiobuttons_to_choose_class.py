from tkinter import *
from Encode_and_Decode_CesarClass import EncodeCesarClass, DecodeCesarClass
from Encode_and_Decode_VigenereClass import EncodeVigenereClass, DecodeVigenereClass
from Encode_and_Decode_VernamClass import CodeVernamClass
from AutomaticHackingCesarCipher import AutomaticCesarClass


def radiobutton_encode_and_decode_class(text_file, window, bg_color):
    r_var = IntVar()

    rad0 = Radiobutton(window, text='зашифровать кодом Цезаря ', value=0,
                       variable=r_var, justify=LEFT, bg=bg_color)
    rad1 = Radiobutton(window, text='зашифровать кодом Виженера', value=1,
                       variable=r_var, justify=LEFT, bg=bg_color)
    rad2 = Radiobutton(window, text='зашифровать кодом Вернама', value=2,
                       variable=r_var, justify=LEFT, bg=bg_color)
    rad3 = Radiobutton(window, text='расшифровать кодом Цезаря', value=3,
                       variable=r_var, justify=RIGHT, bg=bg_color)
    rad4 = Radiobutton(window, text='расшифровать кодом Виженера', value=4,
                       variable=r_var, justify=RIGHT, bg=bg_color)
    rad5 = Radiobutton(window, text='расшифровать кодом Вернама', value=5,
                       variable=r_var, justify=RIGHT, bg=bg_color)
    rad6 = Radiobutton(window, text='автоматический взлом шифра Цезаря частотным анализом', value=6,
                       variable=r_var, justify=CENTER, bg=bg_color)

    rad0.grid(column=0, row=3)
    rad1.grid(column=0, row=4)
    rad2.grid(column=0, row=5)
    rad3.grid(column=2, row=3)
    rad4.grid(column=2, row=4)
    rad5.grid(column=2, row=5)
    rad6.grid(column=1, row=6)

    def choice():
        code_class = [EncodeCesarClass, EncodeVigenereClass, CodeVernamClass,
                      DecodeCesarClass, DecodeVigenereClass, CodeVernamClass, AutomaticCesarClass]
        a = code_class[r_var.get()](text_file, window=window)
        code_text = a.code()
        lbl_code_text = Label(text=code_text)
        lbl_code_text.grid(column=0, row=20)

    click = Button(window, text="Кодировать!!!", command=choice, justify=CENTER, bg=bg_color)
    click.grid(column=1, row=7)
