from fridge import Fridge


if __name__ == "__main__":
    my_fridge = Fridge()
    while True:
        st = int(input("\nВведите команду (0 - выход, 1 - открыть, 2 - закрыть, 3 - изменить температуру, 4 - текущая температура): "))
        print(my_fridge.status(st))
        if st == 0:
            break
        if st == 3:
            temp = int(input(f"Введите значение температуры: минимальное {my_fridge.min_temp}°C - максимальное {my_fridge.max_temp}°C:"))
            now_temp=my_fridge.temperature(temp)
            print(now_temp)
        if st == 4:
            print(my_fridge.get_temperature())
        if my_fridge.open:
            action = input("1 - добавить продукт, 2 - показать содержимое, 3 - удалить продукт: ")
            if action == "1":
                pr = input("Введите название продукта: ")
                print(my_fridge.add_list_products(pr))
            elif action == "2":
                print(my_fridge.add_list_products())
            elif action == "3":
                pr = input("Введите название продукта для удаления: ")
                count = int(input("Введите количество для удаления: "))
                print(my_fridge.del_products(pr, count))