#Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки чередуются). Условный оператор не использовать.
def prinon(N):
    result = 0.0
    for i in range(1, N + 1):
        # Используем (-1) ** (i + 1) для чередования знаков
        result += (i / 10.0) * ((-1) ** (i + 1))
    return result

# Пример использования
N = int(input("Введите целое число N (>0): "))
if N > 0:
    result = prinon(N)
    print(f"Результат выражения: {result}")
else:
    print("N должно быть больше 0.")