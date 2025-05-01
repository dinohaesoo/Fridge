class fridge: 

    def __init__(self):

        self.open = False
        self.products = {}
        self.temp = 3
        self.min_temp = -4
        self.max_temp = 8

    def status(self, st):

        if st == 1:
            if self.open:
                return "Уже открыт!"
            self.open = True
            return "Открыт"
            
        elif st == 2:
            if not self.open:
                return "Уже закрыт!"
            self.open = False
            return "Закрыт"
        
        elif st == 0:
            return "Завершение программы"
        else:
            return ""
        
    def add_list_products(self, pr=None, count=1):

        if self.open:
            if pr is not None:
                if pr in self.products:
                    self.products[pr] += count
                else:
                    self.products[pr] = count
                return f"Добавлен продукт: {pr} (количество: {self.products[pr]})" 

            else:
                if not self.products:
                    return "Нет продуктов"
                return "\n".join(f"{k}: {v}" for k, v in self.products.items())
            
    def del_products(self, pr, count=1):

        if not self.open:
            return "Холодильник закрыт!"
        
        if pr not in self.products:
            return f"Продукта {pr} нет в холодильнике"
        
        if self.products[pr] < count:
            return f"Недостаточно {pr}, в наличии: {self.products[pr]}"
        
        self.products[pr] -= count
        if self.products[pr] == 0:
            del self.products[pr]
            return f"Продукт {pr} полностью удален"
        return f"Удалено {count} {pr}, осталось: {self.products[pr]}"
    
    def temperature (self, temps):

        if temps < self.min_temp:
            return f"Температура не может быть ниже {self.min_temp}°C"
        elif temps > self.max_temp:
            return f"Температура не может быть выше {self.max_temp}°C"
        
        self.temp = temps
        return f"Температура установлена: {self.temp}°C"
    
    def get_temperature(self):
        return f"Текущая температура: {self.temp}°C"
        
if __name__ == "__main__":
    my_fridge = fridge()
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
