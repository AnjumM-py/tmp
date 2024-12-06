#print the quient and reminder
num1 = int(input("Enter the number1 : Number to be devided : "))
num2 = int(input( "enter the number 2: Nember devided by: "))
# Ensuring the divisor is not zero
if num2 !=0:
    quotient = num1 // num2
    remainder = num1 % num2
#dispalying the result
    print(f" the quotient is : {quotient}")
    print (f" the remainder is: {remainder}")
else:
    print("error: Division be zero is not allowed")


