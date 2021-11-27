from KMPsearch import KMPSearch
from datetime import datetime
import time

i = 1
string = input("Введите строку:\n")
while i == 1:
    a = input("Введите желаемую операцию:\nF - найти подстроку\nI - ввести подстроку\nC - сменить строку\nZ - выход\n")
    if a == "i":
        substring = input("Введите подстроку ")
        print("Текущая подстрока - " + substring)
    elif a == "f":
        start_time = datetime.now()
        search = substring in string
        if search:
            time.sleep(0.01)
            end = datetime.now()
            print("Подстрока найдена")
            start_kmp = datetime.now()
            KMPSearch(substring, string)
            time.sleep(0.01)
            end_kmp = datetime.now()
            print("Затраченное время встроенной:", end - start_time)
            print("Затраченное время KMP:", end_kmp - start_kmp)
        else:
            print("Подстрока не найдена")
    elif a == "c":
        string = input("Введите новую строку:\n")
    elif a == "z":
        quit()