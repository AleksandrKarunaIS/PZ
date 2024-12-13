#Составить функцию, которая выполнит суммирования числового ряда.
def grip(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    return sum(numbers[start:end])

# Пример использования
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = grip(numbers, 2, 7)
print("Сумма чисел с индекса 2 по 6:", result)