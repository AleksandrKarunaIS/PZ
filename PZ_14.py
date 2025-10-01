#В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и 
#ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый 
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ. 
import re

with open('dates.txt', 'r', encoding='utf-8') as file:
    content = file.read()

dates_dot = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', content)
dates_slash = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', content)

count_dot = len(dates_dot)
count_slash = len(dates_slash)

with open('dates_slash_only.txt', 'w', encoding='utf-8') as file:
    for date in dates_slash:
        file.write(date + '\n')

print(f"Количество дат в формате ДД.ММ.ГГГГ: {count_dot}")
print(f"Количество дат в формате ДД/ММ/ГГГГ: {count_slash}")

print(f"Все даты в формате ДД/ММ/ГГГГ сохранены в файл 'dates_slash_only.txt'")
