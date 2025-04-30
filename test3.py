# try:
#     x = int(input("Введіть число: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль!")
#

def error_value():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            print("Ви ввели числа:", a, "та", b)
            return a, b
        except ValueError:
            print("Помилка: введено нечислове значення! Спробуйте ще раз.")


def write_line_to_file():
    line = input("Введіть рядок: ")
    with open("output.txt", "w") as file:
        file.write(line)
    print("Рядок записано у файл.")

write_line_to_file()


def count_words_in_file():
    try:
        with open("example.txt", "r") as file:
            text = file.read()
            words = text.split()
            print("Кількість слів у файлі:", len(words))
    except FileNotFoundError:
        print("Файл не знайдено!")

count_words_in_file()


def compare_files():
    try:
        with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            for line in lines1:
                if line not in lines2:
                    print("Унікальний рядок у першому файлі:", line.strip())
    except FileNotFoundError:
        print("Один із файлів не знайдено!")

compare_files()


def read_file():
    try:
        with open("example.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Помилка: файл не знайдено!")

read_file()

def index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[8])
    except IndexError:
        print("Помилка: індекс виходить за межі списку!")

index_error()
