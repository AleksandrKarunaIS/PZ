#Дано целое число N(>1). Вывести наибольшее из целых чисел K, для которых сумма 1+2+...+K будет меньше или равна N, и саму эту сумму
def sum(N):
    K = 0
    total_sum = 0
    
    while True:
        K += 1
        total_sum += K
        if total_sum > N:
            K -= 1  # Уменьшаем K, так как последняя сумма превышает N
            total_sum -= K + 1  # Убираем последний добавленный элемент
            break
    
    return K, total_sum

# Пример использования
N = int(input("Введите целое число N (>1): "))
if N > 1:
    K, total_sum = sum(N)
    print(f"Наибольшее целое число K: {K}")
    print(f"Сумма 1 + 2 + ... + K: {total_sum}")
else:
    print("N должно быть больше 1.")