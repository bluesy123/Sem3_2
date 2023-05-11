
import math

distancePerDay = int(input("Введите кол-во километров за день. "))
distance = int(input("Длина пути. "))

day = (distance + distancePerDay - 1) / distancePerDay
print(day)
