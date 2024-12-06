#taking three input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

#performing operations
addition = num1 + num2 + num3
subtraction = num1 - num2 - num3
multiplication = num1 * num2 * num3
#handling devision by zero

division = None

if num2 !=0 and num3 !=0:
    division = num1 / num2 / num3
else:
    division = "undefined (devision by zero is not allowed)"
#    display(results)
print(f"Addition of the three number is: {addition}")
print(f"Subtraction of three  is: {subtraction}")
print(f"Multiplication of three number is : {multiplication}")
print(f"Division of the three numbsers: {division}")
