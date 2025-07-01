english_russian_dict = {
    "apple": "яблоко",
    "house": "дом",
    "dog": "собака",
    "cat": "кошка",
    "book": "книга",
    "water": "вода",
    "sun": "солнце",
    "tree": "дерево",
    "car": "машина",
    "hello": "привет"
}
def translate_word(word, dictionary):
    return dictionary.get(word.lower(), "Слово не найдено в словаре")
word_to_translate = "dog"
translation = translate_word(word_to_translate, english_russian_dict)
print(f"{word_to_translate} -> {translation}")
print("\nАнгло-русский словарь:")
for eng, rus in english_russian_dict.items():
    print(f"{eng} -> {rus}")