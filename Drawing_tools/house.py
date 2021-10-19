import simple_draw as sd




def triangle(point, length, angle=0):
    for _ in range(3):
        v = sd.get_vector(start_point=point, length=length, angle=angle, width=3)
        v.draw()
        angle += 120
        point = v.end_point


def house(point_x, point_y, color, length, height, row):
    sd.rectangle(right_top=sd.get_point(point_x + length / 2, point_y), left_bottom=sd.get_point(300, 0), color=color,
                 width=2)
    triangle(point=sd.get_point(300, point_y), length=(length * 6.5))
    circle_x = (300 + length * 6.5 / 2)
    h = int(((length * 6.5) ** 2 - (length * 6.5 / 2) ** 2) ** 0.5)
    circle_y = point_y + h / 4
    sd.circle(center_position=sd.get_point(circle_x, circle_y), radius=(h / 8), color=color, width=5)

    for y in range(0, point_y, height):
        row += 1
        for x in range(300, point_x, length):
            x_0 = x if row % 2 else x + length // 2
            left_bottom = sd.get_point(x_0, y)
            right_top = sd.get_point(x_0 + length, y + height)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=color, width=2)





