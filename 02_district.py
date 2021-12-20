# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from pprint import pprint
from district.central_street.house1 import room1 as central1_r1, room2 as central1_r2
from district.central_street.house2 import room1 as central2_r1, room2 as central2_r2

from district.soviet_street.house1 import room1 as soviet1_r1, room2 as soviet1_r2
from district.soviet_street.house2 import room1 as soviet2_r1, room2 as soviet2_r2

population = (central1_r1.folks, central1_r2.folks, central2_r1.folks, central2_r2.folks,
              soviet1_r1.folks, soviet1_r2.folks, soviet2_r1.folks, soviet2_r2.folks)

persons = 'На районе живут: '
for i in population:
    persons += ','.join(i)+','
pprint(persons)
