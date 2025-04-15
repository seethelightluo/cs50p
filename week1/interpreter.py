
expression=input("Enxpression: ")
x, y, z = expression.split(" ")
a={"+","-","*","/"}
if y in a:
    if y=="+":
        print(float(x)+float(z))
    elif y=="-":
        print(float(x)-float(z))
    elif y=="*":
        print(float(x)*float(z))
    elif y=="/":
        print(float(x)/float(z))
    else:
        print("Invalid operator")
