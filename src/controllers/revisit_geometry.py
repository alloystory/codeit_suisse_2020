from flask import jsonify
import math

def get_line(point_1, point_2):
    try:
        m = (point_2["y"] - point_1["y"]) / (point_2["x"] - point_1["x"])
        c = point_1["y"] - m * point_1["x"]
        return (False, m, c)
    except Exception:
        return (True, point_1["x"], None)

def get_intersection(line_1, line_2):
    if line_1[0] and line_2[0]:
        return None
    elif line_2[0]:
        return get_intersection(line_2, line_1)
    elif line_1[0]:
        _, line_1_x, _ = line_1
        _, line_2_m, line_2_c = line_2
        y = line_2_m * line_1_x + line_2_c
        return (line_1_x, y)
    else:
        try:
            _, line_1_m, line_1_c = line_1
            _, line_2_m, line_2_c = line_2

            x = (line_2_c - line_1_c) / (line_1_m - line_2_m)
            y = line_2_m * x + line_2_c
            return (x, y)
        except ZeroDivisionError:
            return None

def is_within_boundaries(x, y, limit_1_x, limit_1_y, limit_2_x, limit_2_y):
    is_x_within = x <= max(limit_1_x, limit_2_x) and x >= min(limit_1_x, limit_2_x)
    is_y_within = y <= max(limit_1_y, limit_2_y) and y >= min(limit_1_y, limit_2_y)
    return is_x_within and is_y_within

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def solve(data):
    shape_coor = data["shapeCoordinates"]
    line_coor = data["lineCoordinates"]
    line = get_line(line_coor[0], line_coor[1])

    results = []
    for i in range(len(shape_coor)):
        for j in range(i, len(shape_coor)):
            if i == j:
                continue
            shape_point_1 = shape_coor[i]
            shape_point_2 = shape_coor[j]

            # Checking if shape line splits points into more than one segments
            # https://stackoverflow.com/questions/1560492/how-to-tell-whether-a-point-is-to-the-right-or-left-side-of-a-line
            signs = set()
            for k, other_point in enumerate(shape_coor):
                if k == i or k == j:
                    continue
                position = sign(
                    (shape_point_1["x"] - shape_point_2["x"]) * (other_point["y"] - shape_point_2["y"]) - 
                    (shape_point_1["y"] - shape_point_2["y"]) * (other_point["x"] - shape_point_2["x"])
                )
                signs.add(position)
            
            if -1 in signs and 1 in signs:
                continue

            # Find intersection
            shape_surface = get_line(shape_point_1, shape_point_2)
            intersection = get_intersection(line, shape_surface)
            if intersection:
                x, y = intersection
                if is_within_boundaries(x, y, shape_point_1["x"], shape_point_1["y"], shape_point_2["x"], shape_point_2["y"]):
                    results.append({
                        "x": x,
                        "y": y
                    })

    return jsonify(results)