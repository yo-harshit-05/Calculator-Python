import math

#Menu
while True:
    print('''\nChoose Operation from the below menu you want to perform
            1 -> Addition
            2 -> Subtract
            3 -> Multiply
            4 -> Divide
            5 -> Floor Division
            6 -> Square
            7 -> Square Root
            8 -> Factorial
            9 -> Percentage
            10-> Exit''')
    ch=int(input("Enter choice here:"))

#Functions
    def add():
        a=float(input("Enter Value for a:"))
        b=float(input("Enter Value for b:"))
        return a+b
    def sub():
        a=float(input("Enter Value for a:"))
        b=float(input("Enter Value for b:"))
        return a-b
    def multiply():
        a=float(input("Enter Value for a:"))
        b=float(input("Enter Value for b:"))
        return a*b
    def division():
        a=float(input("Enter Value for a:"))
        b=float(input("Enter Value for b:"))
        if b==0:
            print("Denominator can't be zero")
        else:
            result=a/b
            return (f"{result:.2f}")
    def fldiv():
        a=float(input("Enter Value for a:"))
        b=float(input("Enter Value for b:"))
        if b==0:
            print("Denominator can't be zero")
        else:
            return a//b
    def square():
        a=float(input("Enter Value for a:"))
        return a**2
    def square_root():
        a=float(input("Enter Value for a:"))
        if a<0:
            print("Negative number square not possible")
        return math.sqrt(a)
    def factorial():
        fact=1
        a=int(input("Enter the value for a:"))
        while a>1:
            fact*=a
            a-=1
        return fact
    def percentage():
        a=int(input("Enter value for a:"))
        b=float(input("Enter how much percent of a you want to calculate:"))
        result=(b/100)*a
        return result
    
#Choices
    if ch==1:
        result=add()
        print("The Addition of a and b is \n",result)
    elif ch==2:
        result=sub()
        print("The Subtraction of a and b is \n",result)
    elif ch==3:
        result=multiply()
        print("The Multiply of a and b is \n",result)
    elif ch==4:
        result=division()
        print("The Division of a and b is \n",result)
    elif ch==5:
        result=fldiv()
        print("The Floor Division of a and b is \n",result)
    elif ch==6:
        result=square()
        print("The Square of a is \n",result)
    elif ch==7:
        result=square_root()
        print("The Square Root of a is \n",result)
    elif ch==8:
        result=factorial()
        print("The factorial of a is \n",result)
    elif ch==9:
        result=percentage()
        print("The percentage of a is \n",result)
    elif ch==10:
        break
    else:
        print("Enter Valid operation ")