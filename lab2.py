import math

def rubles(value):
    per = value // 100
    if per != 0:
        value = value % 100
    if value in [0, 5, 6, 7, 8, 9]:
        return "рублей"
    if value in [2, 3, 4]:
        return "рубля"
    if value == 1:
        return "рубль"
    if value in range(10, 21):
        return "рублей"
    if value >= 21:
        value = value % 10
        if value in [0, 5, 6, 7, 8, 9]:
            return "рублей"
        if value in [2, 3, 4]:
            return "рубля"
        if value == 1:
            return "рубль"

def cents(value) :
    per = value // 100
    if per != 0:
        value = value % 100
    if value in [0, 5, 6, 7, 8, 9]:
        return "копеек"
    if value in [2, 3, 4]:
        return "копейки"
    if value == 1:
        return "копейка"
    if value in range(10, 21):
        return "копеек"
    if value >= 21:
        value = value % 10
        if value in [0, 5, 6, 7, 8, 9]:
            return "копеек"
        if value in [2, 3, 4]:
            return "копейки"
        if value == 1:
            return "копейка"

#value - число, которое нужно вывести
#type - род числа
def numbers(value, type):
    result = ""
    if type == "man":
        mas = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    if type == "girl":
        mas = ["ноль", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    mas2 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    mas3 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    mas4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    per = value // 100
    if per != 0:
        result = result + mas4[per - 1] + " "
        value = value % 100
    if value < 10:
        result = result + mas[value] + " "
    if value >= 11 and value <= 19:
        result += result + mas2[value - 10] + " "
    if value >= 20 and value <= 99:
        whole = value // 10
        drob = value % 10
        result = result + mas3[whole - 2] + " "
        if drob != 0:
            result = result + mas[drob] + " "
    return result


def totl(value):
    drop = 0
    k = -1
    #разбиваем число на число на до и после запятой
    for i in range(len(value)):
        if value[i] == '.':
            k = i

    if k != -1:
        whole = value[0:k]
        drop = value[k + 1: len(value)]
    else:
        whole = value

    whole = int(whole)
    whole_numb = numbers(whole, "man")
    whole_title = rubles(whole)

    drop = int(drop)
    drop_numb = numbers(drop, "girl")
    drop_title = cents(drop)
    result = str(whole_numb) + str(whole_title) + " " + str(drop_numb) + str(drop_title)
    return result

print("Введите цену: ", end="")
spam = str(input())
result = totl(spam)
print(result)