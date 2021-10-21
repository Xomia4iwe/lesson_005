# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd
import Drawing_tools.rainbow as rainbow
import Drawing_tools.sun as sun
import Drawing_tools.house as house
import Drawing_tools.smile as smile
import Drawing_tools.Tree as tree
import Drawing_tools.snowdrift as snowdrift

sd.resolution = (1200, 600)
sun_point = sd.get_point(150, 450)
sun.sun(center_position=sun_point)

rainbow_point = sd.get_point(325, 0)
rainbow.rainbow(point=rainbow_point, radius=800, step=10)

house_point_x = 600
house_point_y = 200
house_color = sd.COLOR_DARK_YELLOW
house_length = 50
house_height = 25
house_row = 0
house.house(point_x=house_point_x, point_y=house_point_y, color=house_color, length=house_length,
            height=house_height, row=house_row)

smile_point = sd.get_point(700, 100)
smile.smile(point1=smile_point)

tree_point = sd.get_point(900, 30)
tree_angle = 90
tree_lenght = 100

tree.tree(start_point_brench=tree_point, angle_brench=tree_angle, lenght_brench=tree_lenght)


snowdrift.snowdrift(x=200, y=10, lenght=20, n=30)


sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
