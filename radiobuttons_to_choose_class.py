from tkinter import Label, Button, Radiobutton, IntVar, LEFT, RIGHT, CENTER
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

    rad0.pack()
    rad1.pack()
    rad2.pack()
    rad3.pack()
    rad4.pack()
    rad5.pack()
    rad6.pack()

    def choice():
        code_class = [EncodeCesarClass, EncodeVigenereClass, CodeVernamClass,
                      DecodeCesarClass, DecodeVigenereClass, CodeVernamClass, AutomaticCesarClass]
        Client_choice_of_encryptor = code_class[r_var.get()](text_file, window=window, bg_color=bg_color)
        code_text = Client_choice_of_encryptor.code()

        lbl_space = Label(text='', bg=bg_color)
        lbl_space.pack()

        # вывожу зашифрованный обработанный программой текст
        lbl_code_text = Label(text=code_text, bg=bg_color)
        lbl_code_text.pack()

    click = Button(window, text="Кодировать!!!", command=choice, justify=CENTER, bg=bg_color)
    click.pack()

    lbl_space = Label(text='', bg=bg_color)
    lbl_space.pack()
