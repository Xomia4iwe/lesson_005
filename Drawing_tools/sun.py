import simple_draw as sd


def sun(center_position, radius=50, color=sd.COLOR_YELLOW):
    sd.circle(center_position, radius, color, width=0)
    angle = 0
    while angle <= 360:
        sd.vector(start=center_position, angle=angle, length=125, color=color, width=3)
        angle += 36

