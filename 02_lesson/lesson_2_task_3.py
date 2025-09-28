def square(side):
    area = side * side
    if side == int(side):
        return int(area)
    else:
        return int(area) + 1

print(square(5))



