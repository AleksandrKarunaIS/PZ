import random

rows = 5
cols = 5
matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for row in matrix:
    print(row)

N = int(input(f"Введите номер столбца (от 0 до {cols - 1}): "))

if 0 <= N < cols:
    column = [row[N] for row in matrix]

    sum_col = sum(column)
    product_col = 1
    for num in column:
        product_col *= num

    print(f"\nСтолбец {N}: {column}")
    print(f"Сумма элементов: {sum_col}")
    print(f"Произведение элементов: {product_col}")
else:
    print("Некорректный номер столбца!")