#Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое, 
#количество пробельных символов. Сформировать новый файл, в который поместить текст 
#в стихотворной форме предварительно вставив после каждой строки строку из символов 
#«*».
poem = """Изведал враг в тот день немало,
Что значит русский бой удалый,
Наш рукопашный бой!..
Земля тряслась – как наши груди,
Смешались в кучу кони, люди,
И залпы тысячи орудий
Слились в протяжный вой..."""

with open('text18-12.txt', 'w', encoding='utf-8') as f:
    f.write(poem)

with open('text18-12.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    space_count = content.count(' ') + content.count('\n')  # Пробелы и переносы строк

    print("Содержимое файла:")
    print(content)
    print(f"\nКоличество пробельных символов: {space_count}")

with open('poem_with_stars.txt', 'w', encoding='utf-8') as f:
    for line in poem.split('\n'):
        f.write(line + '\n')
        f.write('*' * len(line) + '\n')


print("\nФайл poem_with_stars.txt создан с добавленными строками из '*'.")
