# хеш таблица

"""Хеш-таблица (или словарь в Python) - это структура данных, используемая для хранения пар ключ-значение, где каждый ключ уникален. 
Она предоставляет эффективный способ хранения и поиска значений по ключу."""



class HashTable:
    def __init__(self, size):
        # Инициализация хеш-таблицы заданного размера
        self.size = size
        # Создание пустой хеш-таблицы, представленной списком списков
        self.hash_table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # Функция для вычисления хеша ключа, используется простое взятие остатка
        return key % self.size

    def insert(self, key, value):
        # Вычисление хеша для ключа
        hash_key = self._hash_function(key)
        # Поиск внутри списка элементов с ключом key
        for pair in self.hash_table[hash_key]:
            # Если найден элемент с таким ключом, обновляем его значение и завершаем функцию
            if pair[0] == key:
                pair[1] = value
                return
        # Если элемент с таким ключом не найден, добавляем новую пару ключ-значение в список
        self.hash_table[hash_key].append([key, value])

    def delete(self, key):
        # Вычисление хеша для ключа
        hash_key = self._hash_function(key)
        # Поиск элемента с заданным ключом и его удаление из списка
        for i, pair in enumerate(self.hash_table[hash_key]):
            if pair[0] == key:
                del self.hash_table[hash_key][i]
                return

    def search(self, key):
        # Вычисление хеша для ключа
        hash_key = self._hash_function(key)
        # Поиск элемента с заданным ключом в соответствующем списке
        for pair in self.hash_table[hash_key]:
            # Если элемент найден, возвращаем его значение
            if pair[0] == key:
                return pair[1]
        # Если элемент не найден, возвращаем None
        return None

# Пример использования
# Создаем новую хеш-таблицу размером 10
hash_table = HashTable(10)
# Вставляем элемент с ключом 5 и значением "apple" в хеш-таблицу
hash_table.insert(5, "apple")
# Вставляем элемент с ключом 2 и значением "banana" в хеш-таблицу
hash_table.insert(2, "banana")
# Вставляем элемент с ключом 15 и значением "orange" в хеш-таблицу
hash_table.insert(15, "orange")

# Выводим значение элемента с ключом 5, ожидаем "apple"
print(hash_table.search(5))  # Выведет: apple
# Выводим значение элемента с ключом 2, ожидаем "banana"
print(hash_table.search(2))  # Выведет: banana
# Выводим значение элемента с ключом 15, ожидаем "orange"
print(hash_table.search(15)) # Выведет: orange

# Удаляем элемент с ключом 2 из хеш-таблицы
hash_table.delete(2)
# Пытаемся найти элемент с ключом 2, ожидаем None, так как он был удален
print(hash_table.search(2))  # Выведет: None, так как элемент с ключом 2 был удален