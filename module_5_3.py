class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        # Возвращаем новый объект House с увеличенным количеством этажей
        return House(self.name, self.number_of_floors + value)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей {self.number_of_floors}'

    def __iadd__(self, other):
        return self.__add__(other)  # Используем __add__

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)  # Выводит информацию о первом доме
print(h2)  # Выводит информацию о втором доме
print(h1 == h2)  # Сравнение этажей (__eq__)
h1 = h1 + 10  # Увеличиваем количество этажей у h1 (__add__)
print(h1)  # Выводим информацию о h1 после добавления этажей
print(h1 == h2)  # Повторное сравнение этажей
h1 += 10
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__