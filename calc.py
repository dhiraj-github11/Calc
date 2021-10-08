a=int(input("Enter the number to do the operation:"))
b=int(input("Enter the second number to do the operation:"))
c=input("Enter which operation to be done (+,-,/,*):");
def add(a,b):#Addition
    return a+b
def sub(a,b):#Subtraction
    return a-b
def multiply(a,b):#Multiplication
    return a*b
def divide(a,b):#Division
    return a/b
if c=="+":
    print(add(a,b))
if c=="-":
    print(sub(a,b))
if c=="/":
    print(divide(a,b))
if c=="*":
    print(multiply(a,b))


