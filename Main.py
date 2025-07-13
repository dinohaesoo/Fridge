from Fridge import Fridge
from Error import CommandError, TempError, ShelfError, ProductError
import logging

logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

if __name__ == "__main__":
    my_fridge = Fridge()
    while True:
        try:
            st = int(input("Введите команду (0 - выход, 1 - открыть, 2 - закрыть, 3 - изменить температуру, 4 - текущая температура): "))
            print(my_fridge.set_status(st))

            if not (0 <= st <= 4):
                raise CommandError
            if st == 0:
                break

            if st == 3:
                try:
                    temp = int(input(f"Введите значение температуры: минимальное {my_fridge.min_temp}°C - максимальное {my_fridge.max_temp}°C:"))
                    print(my_fridge.set_temperature(temp))
                except TempError:
                    logging.error(f"Температура должна быть между {my_fridge.min_temp}°C и {my_fridge.max_temp}°C")
                except ValueError:
                    logging.error("Неверный формат")

            if st == 4:
                print(my_fridge.get_temperature())
            try:
                if my_fridge.open:
                    try:
                        action = int(input("1 - добавить на полку, 2 - показать содержимое полки, 3 - удалить продукт с полки: "))

                        if not (1 <= action <= 3):
                            raise CommandError

                        if action == 1:
                            try:
                                shelf = int(input("Номер полки (0-2): "))
                                if shelf < 0:
                                    raise ShelfError
                                product = input("Название продукта: ")
                                cnt = int(input("Количество: "))
                                if cnt < 0:
                                    raise ProductError
                                print(my_fridge.add_products_shelf(shelf, product, cnt))
                            except ProductError:
                                logging.error("Количество не может быть отрицательным")
                            except ValueError:
                                logging.error("Неверный формат ввода")
                            except ShelfError:
                                logging.error("Неверный номер полки")

                        elif action == 2:
                            try:
                                shelf = int(input("Номер полки (0-2): "))
                                print(my_fridge.get_products_shelf(shelf))
                            except ShelfError:
                                logging.error("Неверный номер полки")


                        elif action == 3:
                            try:
                                shelf = int(input("Номер полки (0-2): "))
                                if shelf < 0:
                                    raise ShelfError
                                product = input("Название продукта: ")
                                cnt = int(input("Количество: "))
                                if cnt < 0:
                                    raise ProductError
                                print(my_fridge.del_products_shelf(shelf, product, cnt))
                            except ProductError:
                                logging.error("Количество не может быть отрицательным")
                            except ValueError:
                                logging.error("Неверный формат")
                            except ShelfError:
                                logging.error("Неверный номер полки")      
                    except ValueError:
                        logging.error("Неверный формат")   
            except CommandError:
                logging.error("Введите команду от 1 до 3 ")
        except CommandError:
            logging.error("Введите команду от 1 до 4 ")
        except ValueError:
            logging.error("Неверный формат")
