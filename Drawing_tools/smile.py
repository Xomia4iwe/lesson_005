import random

import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.




def smile(point1):
    point2 = sd.get_point(point1.x + 100, point1.y + 75)
    point3 = sd.get_point(point1.x + 35, point1.y + 50)
    point4 = sd.get_point(point1.x + 70, point1.y + 50)
    point_list = [
        sd.get_point(point1.x + 35, point1.y + 35),
        sd.get_point(point1.x + 45, point1.y + 20),
        sd.get_point(point1.x + 60, point1.y + 20),
        sd.get_point(point1.x + 70, point1.y + 35),
    ]
    sd.lines(point_list, color=sd.COLOR_RED)
    sd.ellipse(left_bottom=point1, right_top=point2, color=sd.COLOR_GREEN, width=1)
    sd.circle(center_position=point3, radius=10, color=sd.COLOR_RED, width=3)
    sd.circle(center_position=point4, radius=10, color=sd.COLOR_RED, width=3)
    sd.vector(start=sd.get_point(point1.x + 50, 100), angle=-90, length=60, color=sd.COLOR_GREEN, width=3)
    sd.vector(start=sd.get_point(point1.x + 50, 80), angle=30, length=30, color=sd.COLOR_GREEN, width=3)
    sd.vector(start=sd.get_point(point1.x + 50, 80), angle=-120, length=30, color=sd.COLOR_GREEN, width=3)
    sd.vector(start=sd.get_point(point1.x + 50, 40), angle=-120, length=40, color=sd.COLOR_GREEN, width=3)
    sd.vector(start=sd.get_point(point1.x + 50, 40), angle=-60, length=40, color=sd.COLOR_GREEN, width=3)
