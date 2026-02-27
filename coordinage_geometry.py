x1 = int(input("enter x1: "))
x2 = int(input("enter x2: "))
y1 = int(input("enter y1: "))
y2 = int(input("enter y2: "))

distance = int((((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1)))) 


finalDistance = (distance ** (1/2))

print(finalDistance)
