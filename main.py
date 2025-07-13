from fridge import Fridge
from error import ComandError, TempError, ProductError
import logging

logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

if __name__ == "__main__":
    my_fridge = Fridge()
    while True:
        try:
            st = int(input("Введите команду (0 - выход, 1 - открыть, 2 - закрыть, 3 - изменить температуру, 4 - текущая температура): "))
            logging.info(my_fridge.set_status(st))

            if not (0 <= st <= 4):
                raise ComandError
            
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
                        action = int(input("1 - добавить продукт, 2 - показать содержимое, 3 - удалить продукт: "))

                        if not (1 <= action <= 3):
                            raise ComandError
                        
                        if action == 1:
                            pr = input("Введите название продукта: ")

                            if not pr:
                                raise ValueError   
                            print(my_fridge.add_list_products(pr))

                        elif action == 2:
                            print(my_fridge.get_list_products())

                        elif action == 3:
                            pr = input("Введите название продукта для удаления: ")

                            if not pr:
                                raise ValueError
                            
                            try:
                                count = int(input("Введите количество для удаления: "))

                                if count <= 0:
                                    raise ValueError
                                
                                if count > my_fridge.products[pr]:
                                    raise ProductError
                                
                                if pr not in my_fridge.products:
                                    raise KeyError(f"Продукта '{pr}' нет в холодильнике")
                                print(my_fridge.del_products(pr, count))
                                
                            except ValueError:
                                logging.error("Неверный формат") 
                            except ProductError:
                                logging.error(f"Недостаточно {pr}, в наличии: {my_fridge.products[pr]}")  
                            except KeyError:
                                logging.error(f"Продукта {pr} нет в холодильнике")
                    except ValueError:
                        logging.error("Неверный формат")   
            except ComandError:
                logging.error("Введите команду от 1 до 3 ")
        except ComandError:
            logging.error("Введите команду от 1 до 4 ")
        except ValueError:
            logging.error("Неверный формат")