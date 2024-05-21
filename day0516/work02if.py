x = 9
y = 12
z = 4

# 주어진 값들을 비교하여 낮은 값을 찾아내는 함수
def find_minimum(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

# 주어진 값들 중에서 최솟값을 찾아서 출력하고 그 값을 None으로 바꿔주는 함수
def print_and_replace_minimum(a, b, c):
    min_value = find_minimum(a, b, c)
    print(min_value)
    if min_value == a:
        a = None
    elif min_value == b:
        b = None
    else:
        c = None
    return a, b, c

# 주어진 값들 중에서 가장 작은 값을 차례대로 출력
while x is not None or y is not None or z is not None:
    x, y, z = print_and_replace_minimum(x, y, z)
    if x is None and y is None and z is None:
        break





