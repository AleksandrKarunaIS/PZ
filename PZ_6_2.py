#Дан список размера N. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы в порядке возрастания их индексов.
def pip(arr):
    max_sum = float('-inf')
    max_pair = (None, None)

    for i in range(len(arr) - 1):
        current_sum = arr[i] + arr[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_pair = (arr[i], arr[i + 1])

    return tuple(sorted(max_pair))

# Пример использования функции
arr = [1, 9, 3, 4, 5, 2]
max_pair_sorted = pip(arr)
print(max_pair_sorted)