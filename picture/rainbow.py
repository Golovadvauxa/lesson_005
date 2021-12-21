import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def draw_rainbow():
    radius = 1300
    point = sd.get_point(950, -500)
    for color in rainbow_colors:
        sd.circle(point, radius, color, 10)
        radius -= 10
