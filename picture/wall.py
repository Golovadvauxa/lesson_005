import simple_draw as sd


def draw_brick():
    point = sd.get_point(250, 50)
    v1 = sd.get_vector(start_point=point, angle=90, length=350, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=0, length=700, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=270, length=350, width=3)
    v4 = sd.get_vector(start_point=v3.end_point, angle=180, length=700, width=3)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()

    x1, y1 = 250, 50
    x2, y2 = 350, 100
    point1 = sd.get_point(x1, y1)
    point2 = sd.get_point(x2, y2)
    for i in range(50, 351, 50):
        y1 = i
        y2 = i + 50
        for j in range(250, 851, 50):
            if i % 20 != 0 and j % 20 == 0:
                x1 = j
                x2 = j + 100
                point1 = sd.get_point(x1, y1)
                point2 = sd.get_point(x2, y2)
                sd.rectangle(point1, point2, width=3)
            elif i % 20 == 0 and j % 20 != 0:
                x1 = j
                x2 = j + 100
                point1 = sd.get_point(x1, y1)
                point2 = sd.get_point(x2, y2)
                sd.rectangle(point1, point2, width=3)

    sd.pause()
