import sqlite3
from datetime import datetime
from tabulate import tabulate


# Создание базы данных
def create_database():
    conn = sqlite3.connect('tv_repair.db')
    c = conn.cursor()

    # Создание таблицы ремонтов
    c.execute('''CREATE TABLE IF NOT EXISTS repairs
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     tv_brand
                     TEXT
                     NOT
                     NULL,
                     serial_number
                     TEXT
                     NOT
                     NULL,
                     problem
                     TEXT
                     NOT
                     NULL,
                     repair_date
                     TEXT
                     NOT
                     NULL,
                     document
                     TEXT,
                     master
                     TEXT
                     NOT
                     NULL,
                     repair_cost
                     REAL
                     NOT
                     NULL
                 )''')

    conn.commit()
    conn.close()


# Добавление записи о ремонте
def add_repair():
    print("\nДобавление нового ремонта:")
    tv_brand = input("Марка телевизора: ")
    serial_number = input("Серийный номер: ")
    problem = input("Неисправность: ")
    repair_date = datetime.now().strftime("%Y-%m-%d")
    document = input("Документ (накладная/акт): ")
    master = input("Мастер: ")
    repair_cost = float(input("Сумма оплаты: "))

    conn = sqlite3.connect('tv_repair.db')
    c = conn.cursor()

    c.execute(
        "INSERT INTO repairs (tv_brand, serial_number, problem, repair_date, document, master, repair_cost) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (tv_brand, serial_number, problem, repair_date, document, master, repair_cost))

    conn.commit()
    conn.close()
    print("Запись о ремонте успешно добавлена!")


# Просмотр всех ремонтов
def view_repairs():
    conn = sqlite3.connect('tv_repair.db')
    c = conn.cursor()

    c.execute("SELECT * FROM repairs")
    repairs = c.fetchall()

    if not repairs:
        print("Нет записей о ремонтах.")
    else:
        headers = ["ID", "Марка", "Серийный номер", "Неисправность", "Дата", "Документ", "Мастер", "Сумма"]
        print(tabulate(repairs, headers=headers, tablefmt="grid"))

    conn.close()


# Поиск ремонтов по критериям
def search_repairs():
    print("\nПоиск ремонтов:")
    print("1. По марке телевизора")
    print("2. По серийному номеру")
    print("3. По мастеру")
    print("4. По дате ремонта")
    choice = input("Выберите критерий поиска (1-4): ")

    conn = sqlite3.connect('tv_repair.db')
    c = conn.cursor()

    if choice == '1':
        brand = input("Введите марку телевизора: ")
        c.execute("SELECT * FROM repairs WHERE tv_brand LIKE ?", ('%' + brand + '%',))
    elif choice == '2':
        serial = input("Введите серийный номер: ")
        c.execute("SELECT * FROM repairs WHERE serial_number LIKE ?", ('%' + serial + '%',))
    elif choice == '3':
        master = input("Введите имя мастера: ")
        c.execute("SELECT * FROM repairs WHERE master LIKE ?", ('%' + master + '%',))
    elif choice == '4':
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        c.execute("SELECT * FROM repairs WHERE repair_date = ?", (date,))
    else:
        print("Неверный выбор.")
        return

    results = c.fetchall()

    if results:
        headers = ["ID", "Марка", "Серийный номер", "Неисправность", "Дата", "Документ", "Мастер", "Сумма"]
        print(tabulate(results, headers=headers, tablefmt="grid"))
    else:
        print("Ремонты не найдены.")

    conn.close()


# Главное меню
def main_menu():
    create_database()

    while True:
        print("\nТЕЛЕМАСТЕРСКАЯ - система учета ремонтов")
        print("1. Добавить запись о ремонте")
        print("2. Просмотреть все ремонты")
        print("3. Поиск ремонтов")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            add_repair()
        elif choice == '2':
            view_repairs()
        elif choice == '3':
            search_repairs()
        elif choice == '4':
            print("Работа программы завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()