#.Организовать и вывести последовательность из N случайных целых чисел. Из 
#исходной последовательности организовать новую последовательность, содержащую 
#положительные числа. Найти их количество. 
import random

N = 15  # Можно изменить количество чисел
numbers = [random.randint(-100, 100) for _ in range(N)]

positive_numbers = [num for num in numbers if num > 0]
count_positive = len(positive_numbers)

print("Исходная последовательность:", numbers)
print("Положительные числа:", positive_numbers)

print("Количество положительных чисел:", count_positive)
