file_path = input("Введите путь к файлу: ")
try:
    with open("file_path","r", encoding="UTF=8") as file:
        data = file.read()
        print ("Файл прочитан, ты красавчик")
except FileNotFoundError:
    print ("Файл не найден")

