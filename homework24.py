# задача
# реализовать класс
# Класс Snowflake
# Атрибуты: размер, форма.
# Методы: change_size(new_size), change_shape(new_shape).
# НЕОБЯЗАТЕЛЬНО: Интерфейс для изменения размера и формы снежинки

class Snowflake:
    def __init__(self, size, shape):
        self.size = size
        self.shape = shape

    def change_size(self, new_size):
        self.size = new_size
        print(f'размер изменен {self.size}')

    def change_shape(self, new_shape):
        self.shape = new_shape
        print(f'форма изменена {self.shape}')

    def display(self):
        print(f'снежинка: размер - {self.size}, форма - {self.shape}')

snowflake1 = Snowflake(size='маленькая', shape='звезда')
snowflake1.display()
