def summa():
    try:
        a = int(input("Введите первое число "))
        b = int(input("Введите второе число "))
        print("Результат ",a + b)
    except ValueError:
        print("Надо вводить число") 
def vychit():
    try:
        a = int(input("Введите первое число "))
        b = int(input("Введите второе число "))
        print("Результат ", a - b)
    except ValueError:
        print("Надо вводить число")
def umnozh():
    try:
        a = int(input("Введите первое число "))
        b = int(input("Введите второе число "))
        print("Результат ", a * b)
    except ValueError:
        print("Надо вводить число")
def deleniye():
    try:    
        a = int(input("Введите первое число "))
        b = int(input("Введите второе число "))
        if b==0:
            print("На ноль делить нельзя")
        else:
            print("Результат ", a / b)
    except ValueError:
        print("Надо вводить число")
def stepen():
    try:
        a = int(input("Введите число "))
        b = int(input("Введите степень "))
        print("Результат ", a ** b)
    except ValueError:
        print("Надо вводить число")
def koren():
    try:
        a = int(input("Введите число "))
        print("Результат ",a**0.5)
    except ValueError:
        print("Надо вводить число")    
def factorial():
    try:
        a = int(input("Введите число "))
        if a>0:
            print("Результат ",math.factorial(a))
        else:
            print("Число должно быть больше 0")
    except ValueError:
        print("Надо вводить число")
def sinus():
    try:
        a = int(input("Введите угол(в градусах) "))
        a = math.radians(a)
        print("Результат ",math.sin(a))
    except ValueError:
        print("Надо вводить число")
def cosinus():
    try:
        a = int(input("Введите угол(в градусах) "))
        a = math.radians(a)
        print("Результат ",math.cos(a))
    except ValueError:
        print("Надо вводить число")
def tangens():
    try:
        a = int(input("Введите угол(в градусах) "))
        a = math.radians(a)
        print("Результат ", math.tan(a))
    except ValueError:
        print("Надо вводить число")
import math
while (True):
    print("Выберите действие:")
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")
    print("5.Возведение в степень")
    print("6.Квадратный корень")
    print("7.Факториал")
    print("8.Синус")
    print("9.Косинус")
    print("10.Тангенс")
    print("11.Выход из программы")
    try:
        choice = int(input())
    except ValueError:
        print("Надо вводить число")
    match choice:
        case 1:
            summa()
        case 2:
            vychit()
        case 3:
            umnozh()
        case 4:
            deleniye()
        case 5:
            stepen()
        case 6:
            koren()
        case 7:
            factorial()
        case 8:
            sinus()
        case 9:
            cosinus()
        case 10:
            tangens()
        case 11:
            break