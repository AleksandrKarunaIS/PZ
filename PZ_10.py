stores = {
    "Магнит": {"молоко", "соль", "сахар", "печенье", "сыр"},
    "Пятерочка": {"мясо", "молоко", "сыр"},
    "Перекресток": {"молоко", "творог", "сыр", "сахар", "печенье"},
    "Лента": {"печенье", "молоко", "сыр", "сметана"}
}
no_smetana = [store for store, products in stores.items() if "сметана" not in products]
print("1. Магазины, где нельзя приобрести сметану:", ", ".join(no_smetana))
magnit_minus_perekrestok = stores["Магнит"] - stores["Перекресток"]
print("2. Товары из Магнит, отсутствующие в Перекресток:", ", ".join(magnit_minus_perekrestok))
lenta_minus_magnit = stores["Лента"] - stores["Магнит"]
print("3. Товары из Лента, отсутствующие в Магнит:", ", ".join(lenta_minus_magnit))