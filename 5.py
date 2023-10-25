products = {
    "Масло моторное": ["Синтетическое масло для двигателя", 25.0, 100],
    "Фильтр масляный": ["Фильтр масляный для двигателя", 5.0, 50],
    "Тормозные колодки": ["Тормозные колодки для передних колес", 20.0, 30],
    "Свечи зажигания": ["Свечи зажигания NGK", 3.0, 60],
    "Аккумулятор": ["Аккумуляторная батарея 12V", 50.0, 20],
}

total = 0

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Введите номер пункта меню: ")

    if choice == "1":
        for product, info in products.items():
            print(f"{product} - {info[0]}")

    elif choice == "2":
        for product, info in products.items():
            print(f"{product} - {info[1]} руб.")

    elif choice == "3":
        for product, info in products.items():
            print(f"{product} - {info[2]} шт.")

    elif choice == "4":
        for product, info in products.items():
            print(f"{product} - {info[0]}, Цена: {info[1]} руб., Количество: {info[2]} шт.")

    elif choice == "5":
        product_name = input("Введите название продукции (или 'n' для завершения покупок): ")
        if product_name == "n":
            break
        if product_name in products:
            quantity = int(input("Введите количество: "))
            if quantity <= products[product_name][2]:
                products[product_name][2] -= quantity
                total += products[product_name][1] * quantity
                print(f"Добавлено в корзину: {product_name} (x{quantity})")
            else:
                print("Недостаточно товара на складе.")
        else:
            print("Такой продукции нет в магазине.")

    elif choice == "6":
        print(f"Общая стоимость покупки: {total} руб.")
        print("Остаток на складе:")
        for product, info in products.items():
            print(f"{product} - {info[2]} шт.")
        break

    else:
        print("Пожалуйста, выберите правильный пункт меню.")