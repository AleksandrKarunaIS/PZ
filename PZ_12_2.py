names = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']

short_names = [name for name in names if len(name) <= 5]

print("Исходный список имен:", names)
print("Имена длиной не более 5 символов:", short_names)