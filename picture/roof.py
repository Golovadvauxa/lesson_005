import simple_draw as sd


def draw_roof():
    point_start = sd.get_point(220, 350)
    point_end = sd.get_point(980, 350)
    point_top = sd.get_point(600, 450)

    sd.line(start_point=point_start, end_point=point_end, color=sd.COLOR_RED, width=10)
    sd.line(start_point=point_start, end_point=point_top, color=sd.COLOR_RED, width=10)
    sd.line(start_point=point_top, end_point=point_end, color=sd.COLOR_RED, width=10)

    sd.pause()
