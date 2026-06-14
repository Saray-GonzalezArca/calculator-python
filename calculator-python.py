operation = input("Chose the operation: sum, substract, multiply or divide: ")
num1 = int(input("Type in the first number: "))
num2 = int(input("Type in the second number: "))

if operation == "sum":
    print(num1+num2)
elif operation == "substract":
    print(num1-num2)
elif operation == "multiply":
    print(num1/num2)
else:
    print(num1*num2)