def sum_digits(number):
    sum = 0
    while (number!=0):
        sum=sum + (number%10)
        number=number//10
    return number
x = int(input())
print("Сумма цифр ",x," равна ",sum_digits(x))