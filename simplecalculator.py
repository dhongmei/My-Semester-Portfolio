#Daniel Mei
#11/19/24
#simple calc

#Init


#Function
def add(num1, num2): #add
    result = num1+num2
    print("The result is:" + str(result))
def subtract(num1,num2): #sub
    result = num1-num2
    print("The result is:" + str(result))
def multiply(num1, num2): #mutiply
    result = num1*num2
    print("The result is:" + str(result))
def divide(num1, num2): #divide
    result = num1/num2
    print("The result is:" + str(result))
def simpleCalculator(): #main calculator
    print("Welcome Preschoolers to Simple Calculator") #intro
    print("Enter an operation:")    #users imput
    while True:     #loops
        print("""1.Addition
2.Subtraction
3.Division
4.Multiplication
5.Quit""")
        operation = int(input("What operation would you like to perform:"))
        if operation == 1: # True
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your sencond number:"))
            add (int1,int2)
        if operation == 2: # True
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your sencond number:"))
            subtract(int1,int2)
        if operation == 3: # True
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your sencond number:"))
            multiply (int1,int2)
        if operation == 4:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your sencond number:"))
            divide (int1,int2)
        if operation == 5:
            break
#main
simpleCalculator()
