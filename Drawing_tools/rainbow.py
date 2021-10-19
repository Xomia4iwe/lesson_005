import simple_draw as sd


def rainbow(point, radius, step):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    for i in rainbow_colors:
        radius += step
        sd.circle(center_position=point, radius=radius, width=10, color=i)


