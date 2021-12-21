import simple_draw as sd


def draw_tree(start_point, angle, length):
    if length < 5:
        return
    angle_0 = angle + 90
    angle_1 = angle_0 - 30
    angle_2 = angle_0 + 30
    v1 = sd.get_vector(start_point=start_point, angle=angle_1, length=length)
    v2 = sd.get_vector(start_point=start_point, angle=angle_2, length=length)
    v1.draw()
    v2.draw()
    next_length = length * 0.75
    random_angle1 = sd.random_number(18, 42)
    random_angle2 = sd.random_number(18, 42)
    random_length1 = sd.random_number(6, 9) / 10
    random_length2 = sd.random_number(6, 9) / 10
    draw_branches(start_point=v1.end_point, angle=angle - random_angle1, length=length * random_length1)
    draw_branches(start_point=v2.end_point, angle=angle + random_angle2, length=length * random_length2)


point_tree = sd.get_point(600, 50)
tree = sd.get_vector(start_point=point_tree, angle=90, length=100)
tree.draw(width=5)
draw_tree(start_point=tree.end_point, angle=0, length=100)

sd.pause()
