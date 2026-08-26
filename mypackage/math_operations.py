import math


def factorial(n):
    return math.factorial(n)


def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t


def trigonometry(angle):
    radian = math.radians(angle)

    print("Sin:", math.sin(radian))
    print("Cos:", math.cos(radian))
    print("Tan:", math.tan(radian))


def circle_area(radius):
    return math.pi * radius * radius


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height