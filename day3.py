#Conditional loops 

#Age Checker
def ageChecker():
    age=input("Enter your age : ")

    if age >= "18":
     print(" You are an Adult ")
    else:
     print("You are a minor")


#Number checker
def numberChecker():
    number=input("Enter your number : ")

    if number > "0":
        print("Its a Positive number")
    elif number < "0":
        print("Its a Negative number")
    else:
        print("The number is zero")


#Password Checker

password=input("Enter your password : ")

if password =="admin":
     print("Access granted")
else:
     print("Access denied")


#Multiple numbers 

num1=input("Enter first number :")
num2=input("Enter second number :")

if num1 and num2 > "0":
    print("Both are Positive")
elif num1 and num2 =="0":
    print("Both are Zeros")
else:
    print("Mixed")