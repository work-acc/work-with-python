import math
x1 = int(input("Введите координаты вершина А:"))
y1 = int(input())
x2 = int(input("Введите координаты вершина B:"))
y2 = int(input())
x3 = int(input("Введите координаты вершина C:"))
y3 = int(input())
x4 = int(input("Введите координаты вершина D:"))
y4 = int(input())
S1 = math.fabs((x1-x2)*(y3-y2)-(y1-y2)*(x3-x2))/2
S2 = math.fabs((x1-x4)*(y3-y4)-(y1-y4)*(x3-x4))/2
ABCD = S1 + S2
print("Ответ: ", ABCD)
