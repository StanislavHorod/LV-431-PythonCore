def diskrimim(a,b,c):
    diskrim = b**2 - 4*a*b
    print("Diskriminant D = {}".format(diskrim))
    if diskrim > 0:
        x1 = (-b + (diskrim**0.5)/(2*a))
        x2 = (-b - (diskrim**0.5)/(2*a))
        print("X1 = {}".format(x1) + "\nX2 = {}".format(x2))
    elif diskrim == 0:
        x = -b/(2*a)
        print("x = {}".format(x))
    else:
        print("There is no resaults")

a = float(input("Write coeficients for equation: (ax^2 + bx + c = 0):\na= "))
b = float(input("b= "))
c = float(input("c= "))
diskrimim(a=a, b=b, c=c)