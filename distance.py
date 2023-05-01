import math
x1=int(input("enter the firs abssissa"))
x2=int(input("enter the first ordinate"))
y1=int(input("enter the second abssissa"))
y2=int(input("enter the second ordinate"))
D=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print("Distance is:{}".format(D))
