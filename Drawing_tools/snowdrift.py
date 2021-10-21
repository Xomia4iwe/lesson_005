import simple_draw as sd




def snowdrift(x, y, lenght, n):
    for _ in range(n):
        sd.snowflake(center=sd.get_point(x + sd.random_number(0, 100), y + sd.random_number(0, 150)), length=lenght)
        sd.snowflake(center=sd.get_point(x - sd.random_number(0, 300), y + sd.random_number(0, 60)), length=lenght)





