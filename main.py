from CreatorClientCipherClass import choices


# читаю текст из файла, предусматривая ошибки неправильного ввода пути файла
def except_path_file_errors():
    try:
        path = input("Введите абсолютный путь к файлу: ").strip()
        with open(path, encoding='utf-8', mode='r') as f:
            text = f.read()
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
choices(text).code()
# choices(a).code()
