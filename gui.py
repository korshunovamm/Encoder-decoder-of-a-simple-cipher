from tkinter import *
from tkinter import filedialog
from os import path
from radiobuttons_to_choose_class import radiobutton_encode_and_decode_class


def get_text_from_file():
    file_name = filedialog.askopenfilename(initialdir=path.dirname("~/"),
                                           title='Выберите файл для кодирования',
                                           filetypes=[("Text files", '*.txt')])
    file_text = open(file_name, encoding='utf-8', mode='r')
    text = file_text.read()
    if file_text:
        radiobutton_encode_and_decode_class(text, window, bg_color)
    file_text.close()
    return text


def button_get_text_from_file():
    text_from_file = Button(window, text="Выбрать файл для кодирования",
                            command=get_text_from_file,
                            bg='LightSteelBlue2',
                            justify=CENTER)
    text_from_file.grid(column=1, row=1)
    return text_from_file


window = Tk()
window.title("Вас приветсвтует шифратор")
window.geometry('2400x1400')
window['bg'] = 'LightSteelBlue1'
bg_color = 'LightSteelBlue1'

lbl = Label(window, text="приветственный текст",
            font=("Arial Bold", 20), bg=bg_color)
lbl.grid(column=0, row=0)

# вызов шифратора
button_get_text_from_file()

window.mainloop()
