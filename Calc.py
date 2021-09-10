def add (a,b):
    return a+b


def substract (a,b):
    return a-b


def multiply (a,b):
    return a*b


def divide(a,b):
    return a/b

a=int(input("enter your value - "))
b=int(input("enter your value - "))
c=input("enter the operation to perform (+,-,*,/) - ")

if c=="+":
    print(add(a,b))
elif c=="-":
    print(substract(a,b))
elif c=="*":
    print(multiply(a,b))
elif c=="/":
    print(divide(a,b))
else:
    print("wrong input")


