def calculate_area_rectangle(width, height):
    """计算矩形面积"""
    if width <= 0 or height <= 0:
        raise ValueError("边长必须为正数")
    area = width * height
    return area


def calculate_area_square(side):
    """计算正方形面积"""
    if side <= 0:
        raise ValueError("边长必须为正数")
    area = side * side
    return area


if __name__ == "__main__":
    print(calculate_area_rectangle(5, 3))
    print(calculate_area_square(4))
