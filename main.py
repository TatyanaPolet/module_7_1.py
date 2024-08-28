from pprint import pprint
class Product:        #Класс Product с атрибутами name(строка), weight(дробное число) и category(строка)

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):   #возвращает строку в формате <название>, <вес>, <категория>
        return f'{self.name}, {self.weight}, {self.category}' # через запятую

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'
        
#инкапсулированный атрибут __file_name = 'products.txt'
#метод get_products(self), который считывает всю информацию из файла __file_name,
#закрывает его и возвращает единую строку со всеми товарами из файла __file_name
#метод  add(self, *products), который принимает неограниченное количество объектов класса Product.
#добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле(по названию).
#если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return str(products)

    def add(self, *products):
        file = open(self.__file_name, 'a')
        new_products = self.get_products()
        for product in products:
            if product.name not in new_products:
                file.write(str(product) + '\n')
                new_products += product.name + '\n'
            else:
                print(f'Продукт {product.name} уже есть в магазине.')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
