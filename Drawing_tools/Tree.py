import simple_draw as sd

sd.resolution = (1200, 600)


def tree(start_point_brench, angle_brench, lenght_brench):
    if lenght_brench < 2:
        return

    v1 = sd.get_vector(start_point_brench, angle_brench, lenght_brench, width=4)
    v1.draw(color=sd.COLOR_DARK_ORANGE)
    deviation_size = 30 - (30 * (sd.random_number(0, 40) / 100))
    deviation_size_lenght = .75 - (.75 * (sd.random_number(0, 40) / 100))
    delta_angle_1 = angle_brench - deviation_size
    delta_angle_2 = angle_brench + deviation_size
    next_lenght_branches = lenght_brench * deviation_size_lenght
    tree(start_point_brench=v1.end_point, angle_brench=delta_angle_1, lenght_brench=next_lenght_branches)
    tree(start_point_brench=v1.end_point, angle_brench=delta_angle_2, lenght_brench=next_lenght_branches)




