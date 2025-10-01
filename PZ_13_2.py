#В двумерном списке найти отрицательные элементы, сформировать из них новый 
#массив. Вывести размер полученного массива.
from PZ_13_1 import matrix

negative_elements = [num for row in matrix for num in row if num < 0]

print("\nВсе отрицательные элементы матрицы:", negative_elements)

print("Размер полученного массива:", len(negative_elements))
