#Дано двузначное число. Найти сумму и произведение его цифр
a=int(input('введите двузначное число '))
c = a//10 
e = a%10
d = c + e
r = c * e
print(f"Сумма равна {d} Произведение равно {r}")