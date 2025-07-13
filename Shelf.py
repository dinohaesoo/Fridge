class Shelf:

    __slots__ = ('products', 'open')

    def __init__(self):
        self.products = {}
        self.open = False


    def add_list_products(self, product=None, count=1):

        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count
        #print(hasattr(product, 'dict'))
        return f"Добавлен продукт: {product} (количество: {self.products[product]})"

    def get_list_products(self):

        if not self.products:
            return "Нет продуктов"
        return "\n".join(f"{k}: {v}" for k, v in self.products.items())

    def del_products(self, product, count=1):

        if product not in self.products:
            return f"Продукта {product} нет в холодильнике"

        if self.products[product] < count:
            return f"Недостаточно {product}, в наличии: {self.products[product]}"

        self.products[product] -= count
        if self.products[product] == 0:
            del self.products[product]
            return f"Продукт {product} полностью удален"
        return f"Удалено {count} {product}, осталось: {self.products[product]}"