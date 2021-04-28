from os import path
from tkinter import Tk, Label, filedialog, Button, CENTER
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


def button_get_text_from_file():
    text_from_file = Button(window, text="Выбрать файл для кодирования",
                            command=get_text_from_file,
                            bg='LightSteelBlue2',
                            justify=CENTER)
    text_from_file.pack()
    lb_space = Label(text='', bg=bg_color)
    lb_space.pack()
    return text_from_file


window = Tk()
window.title("Вас приветсвтует шифратор")
window.geometry('1000x1000')
bg_color = 'LightSteelBlue1'
window['bg'] = bg_color

lbl = Label(window, text="""Чтобы шифрование вашего исходного текста прошло успешно рекомендуется выбирать файлы, 
содержащие буквы одного алфавита(латинского/русского), за исключение быть может шифрования/расшифрования шифром Вернама.
Для более детального ознакомления с программой, можно прочитать README.
Автоматический взлом шифра Цезаря не работает на текстах, не содержащих хотя бы одну букву или содеожащих буквы ращного 
алфавита.
Чтобы выбрать файл, нажмите кнопку ниже ;).
""",
            font=("Arial Bold", 10), bg=bg_color)
lbl.pack()

lbl_space = Label(text='', bg=bg_color)
lbl_space.pack()

# вызов шифратора
button_get_text_from_file()

window.mainloop()
