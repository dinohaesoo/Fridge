class Fridge: 

    def __init__(self):

        self.open = False
        self.products = {}
        self.temp = 3
        self.min_temp = -4
        self.max_temp = 8

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
            
        
    def add_list_products(self, pr=None, count=1):

        if pr in self.products:
            self.products[pr] += count
        else:
            self.products[pr] = count
        return f"Добавлен продукт: {pr} (количество: {self.products[pr]})" 

    def get_list_products(self):

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
    
    def set_temperature (self, temps):

        if temps < self.min_temp:
            return f"Температура не может быть ниже {self.min_temp}°C"
        elif temps > self.max_temp:
            return f"Температура не может быть выше {self.max_temp}°C"
        
        self.temp = temps
        return f"Температура установлена: {self.temp}°C"
    
    def get_temperature(self):
        return f"Текущая температура: {self.temp}°C"
