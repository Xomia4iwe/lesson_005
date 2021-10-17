# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as inhabitants_1
from district.central_street.house1 import room2 as inhabitants_2
from district.central_street.house2 import room1 as inhabitants_3
from district.central_street.house2 import room2 as inhabitants_4
from district.soviet_street.house1 import  room1 as inhabitants_5
from district.soviet_street.house1 import  room1 as inhabitants_6
from district.soviet_street.house1 import  room2 as inhabitants_7
from district.soviet_street.house1 import  room2 as inhabitants_8


print('На районе живут: ', ' , '.join(inhabitants_1.folks), ' , '.join(inhabitants_2.folks), ' , '
                                                                                             ''.join(
    inhabitants_3.folks), ' , '.join(inhabitants_4.folks), ' , '.join(inhabitants_5.folks), ' , '
                                                                                            ''.join(
    inhabitants_6.folks), ' , '.join(inhabitants_7.folks), ' , '.join(inhabitants_8.folks))






