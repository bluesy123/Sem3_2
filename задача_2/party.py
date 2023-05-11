
class1 = int(input("Введите кол-во учеников: "))
class2 = int(input("Введите кол-во учеников во 2-м классе "))
class3 = int(input("Введите кол-во учеников в 3-м классе "))

if class1 % 2 != 0:
    x = class1 // 2
else:
    x = class1 / 2 # 10.5
if class2 % 2 != 0:
    y = class2 % 2
else:
    y = class2 / 2
if class3 % 2 != 0:
    z = class3 // 2
else:
    z = class3 / 2
print (round(x + y + z))

