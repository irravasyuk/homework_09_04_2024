# Завдання 1
#  Метаклас, який вносить додаткові перевірки/логіку
# до певних методів у всіх класах.
# class AdditionalLogicMeta(type):
#     def __new__(cls, name, bases, dct):
#         if "method" in dct:
#             original_method = dct["method"]
#
#             def new_method(self, *args, **kwargs):
#                 print('Додаткова логіка перед викликом методу')
#                 result = original_method(self, *args, **kwargs)
#                 print('Додаткова логіка після виклику методу')
#                 return result
#
#             dct['method'] = new_method
#
#         return super().__new__(cls, name, bases, dct)
#
# class MyClass(metaclass=AdditionalLogicMeta):
#     def method(self):
#         print('Оригінальний метод')
#
# my_instance = MyClass()
# my_instance.method()


# Завдання 2
#  Метаклас, що може змінювати ім'я класу залежно
# від певних умов або параметрів.
# class NameMeta(type):
#     def __new__(cls, name, bases, dct):
#         if 'rename_class' in dct and dct['rename_class']:
#             name = f'new_name_{name}'
#
#         return super().__new__(cls, name, bases, dct)
#
#
# class MyClass(metaclass=NameMeta):
#     rename_class = True
#
#
# print(MyClass.__name__)

# Завдання 3
#  Створіть метаклас, який автоматично додає певні
# атрибути до всіх класів, що використовують його.
# class AttributesMeta(type):
#     def __new__(cls, name, bases, dct):
#         dct['attribute1'] = 'value1'
#         dct['attribute2'] = 'value2'
#
#         return super().__new__(cls, name, bases, dct)
#
# class MuClass(metaclass=AttributesMeta):
#     pass
#
# obj = MuClass()
# print(obj.attribute1)
# print(obj.attribute2)

# Завдання 4
# Метаклас, що додає перевірку та обробку аргументів
# __init__ у всіх класах.
class ArgumentProcessing(type):
    def __call__(cls, *args, **kwargs):
        if '__init__' in cls.__dict__:
            original_init = cls.__init__
            def new_init(self, *args, **kwargs):
                print('Перевірка та обробка аргументів')
                original_init(self, *args, **kwargs)
            cls.__init__ = new_init
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=ArgumentProcessing):
    def __init__(self, a, b):
        self.a = a
        self.b = b

obj = MyClass(5, 10)

