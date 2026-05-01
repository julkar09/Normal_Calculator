print(" 0. welcome to the calculator")
print(" 1. addition")
print(" 2. subtraction")
print(" 3. multiplication")
print(" 4. division")   
print(" 5. modulus")
print(" 6. exponentiation")
print(" 7. floor division")

operation  = int(input("enter the operation you want to perform: "))

if operation == 0:
    print("welcome to the calculator")

elif operation == 1:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    result = num1 + num2
    print("the result of addition is: ", result)

elif operation == 2:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    result = num1 - num2
    print("the result of subtraction is: ", result)

elif operation == 3:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    result = num1 * num2
    print("the result of multiplication is: ", result)

elif operation == 4:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print("the result of division is: ", result)
    else:
        print("error: division by zero is not allowed")

elif operation == 5:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    if num2 != 0:
        result = num1 % num2
        print("the result of modulus is: ", result)
    else:
        print("error: modulus by zero is not allowed")

elif operation == 6:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    result = num1 ** num2
    print("the result of exponentiation is: ", result)

elif operation == 7:
    num1= int(input("enter the first number: "))
    num2= int(input("enter the second number: "))
    if num2 != 0:
        result = num1 // num2
        print("the result of floor division is: ", result)
    else:
        print("error: floor division by zero is not allowed")