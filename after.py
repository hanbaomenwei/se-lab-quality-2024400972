def calculate_area(length, width=None):
    """统一计算矩形或正方形的面积
    如果只传入一个参数，则视为正方形边长
    """
    if width is None:
        width = length
    if length <= 0 or width <= 0:
        raise ValueError("边长必须为正数")
    return length * width


if __name__ == "__main__":
    print(calculate_area(5, 3))   # 矩形面积
    print(calculate_area(4))      # 正方形面积
