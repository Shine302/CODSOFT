#Creating the calculator function
def calculator(x,y):
    opp = input("\nEnter an Operator\n(For Addition'+'\n For Subtraction'-'\n For Multiplication'*'\n For Division'/')\n: ")

    if(opp == '+'):
        print("\n{} + {}".format(x,y))
        print("=",x + y)
    elif(opp == '-'):
        print("\n{} - {}".format(x,y))
        print("=",x - y)
    elif(opp == '*'):
        print("\n{} * {}".format(x,y))
        print("=",x * y)
    elif(opp == '/'):
        print("\n{} / {}".format(x,y))
        print("=",x / y)
    else:
        print("Wrong Mathematical Operator")

while 1:

#Title
    print("\nSimple Calculator")
    print("`````````````````")

#Taking two numbers as user input    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

#Calling the calculator function
    calculator(num1,num2)

    