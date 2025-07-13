from Error import TempError, ShelfError
from Shelf import Shelf

class Fridge: 

    __slots__ = ('temp', 'min_temp', 'max_temp', 'shelves', 'open')

    def __init__(self):

        self.temp = 3
        self.min_temp = -4
        self.max_temp = 8
        self.shelves = [Shelf() for _ in range(3)]
        self.open = False

    def set_status(self, st):

        match st:
            case 1:
                if self.open:
                    return "Уже открыт!"
                self.open = True
                return "Открыт"
            case 2:
                if not self.open:
                    return "Уже закрыт!"
                self.open = False
                return "Закрыт"
            case 0:
                return "Завершение программы"
            case _:
                return ""

    def set_temperature (self, temps):

        if temps > self.max_temp or temps < self.min_temp:
            raise TempError
        self.temp = temps
        return f"Температура установлена: {self.temp}°C"

    def get_temperature(self):

        return f"Текущая температура: {self.temp}°C"

    def add_products_shelf(self, shelf_num, product,  count=1):

        if not isinstance(count, int):
            raise ValueError

        if not 0 <= shelf_num < len(self.shelves):
            raise ShelfError
        return self.shelves[shelf_num].add_list_products(product, count)

    def get_products_shelf(self, shelf_num):

        if not 0 <= shelf_num < len(self.shelves):
            raise ShelfError
        return self.shelves[shelf_num].get_list_products()

    def del_products_shelf(self, shelf_num, product, count=1):

        if not isinstance(count, int):
            raise ValueError

        if not 0 <= shelf_num < len(self.shelves):
            raise ShelfError
        return self.shelves[shelf_num].del_products(product, count)
