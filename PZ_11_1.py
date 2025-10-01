#Средствами языка Python сформировать текстовый файл (.txt), содержащий 
#последовательность из целых положительных и отрицательных чисел. Сформировать 
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
#обработку элементов: 
#Исходные данные: 
#Количество элементов: 
#Максимальный элемент: 
#Среднее арифметическое элементов первой трети: 
import random

with open('numbers.txt', 'w', encoding='utf-8') as f:
    numbers = [random.randint(-100, 100) for _ in range(30)]
    f.write(' '.join(map(str, numbers)))

with open('numbers.txt', 'r', encoding='utf-8') as f:
    nums = list(map(int, f.read().split()))

    count = len(nums)
    max_num = max(nums)
    third = len(nums) // 3
    avg_first_third = sum(nums[:third]) / third if third > 0 else 0

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(f"""Исходные данные: {' '.join(map(str, nums))}
Количество элементов: {count}
Максимальный элемент: {max_num}
Среднее арифметическое элементов первой трети: {avg_first_third:.2f}""")


print("Файл report.txt создан с результатами обработки.")
