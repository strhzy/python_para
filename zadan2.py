def is_even(number):
    if number%2==0:
        return True
    else:
        return False
x=int(input("Введите число "))
if is_even(x)==True:
    print("число четное")
else:
    print("число нечетное")