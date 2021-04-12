from CreatorClientCipherClass import choices


# читаю текст из файла, предусматривая ошибки неправильного ввода пути файла
def except_path_file_errors():
    try:
        # читаю абсолютный путь к файлу, убирая пробелы в начале и в конце
        path = input("Введите абсолютный путь к файлу: ").strip()
        # открываю для чтения клиентский файл по формату utf-8 и записываю его содержимое в text
        with open(path, encoding='utf-8', mode='r') as f:
            text = f.read()
        # закрываю файл
        f.close()
        return text
    except FileNotFoundError:
        print("Нет такого файла!")
        except_path_file_errors()
    except IsADirectoryError:
        print("Это каталог!")
        except_path_file_errors()


# вывод шифрования в консоль
text = except_path_file_errors()
a = choices(text).code()
# choices(a).code()
