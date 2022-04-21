# Домашнее задание к лекции #4

## 1. Написать метакласс, который в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_" (+тесты).
  Подменяться должны так же атрибуты экземпляра после создания экземпляра класса (dynamic в примере).

    class CustomMeta():
        pass

    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"

    inst = CustomClass()
    inst.custom_x
    inst.custom_val
    inst.custom_line()
    CustomClass.custom_x
    str(inst) == "Custom_by_metaclass"

    inst.dynamic = "added later"
    inst.custom_dynamic == "added later"

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
    inst.yyy  # ошибка
    CustomClass.x  # ошибка


## 2. Дескрипторы с проверками типов и значений данных (+тесты)
    class Integer:
        pass

    class String:
        pass

    class PositiveInteger:
        pass

    class Data:
        num = Integer()
        name = String()
        price = PositiveInteger()

        def __init__(...):
            ....
