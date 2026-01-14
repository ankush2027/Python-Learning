#Basic I/O

#Input numbers
number=int(input("Enter a number : "))
print("The number is",number)


#Sum
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
print("The sum is",num1+num2)


#Difference
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
print("The difference is",num1-num2)


#Product
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
print("The Product of two numbers",num1*num2)


#Quotient and Remainder
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
quot=num1/num2
rem=num1%num2
print("The Quotient is",quot)
print("The Remainder is",rem)


#String
String=input("Enter a string : ")
print("You entered",String)


#Average
num1=int(input("Enter Num1 : "))
num2=int(input("Enter Num2 : "))
num3=int(input("Enter Num3 : "))

print("The average of three numbers is",(num1+num2+num3)/3)


#Float
number=float(input("Enter a number : "))
print(round(number,2))



#ASCII value
char=input("Enter a character : ")
print(ord(char)) #Or can use char.encode()[0]


#Read ASCII
asci=int(input("Enter a value : "))
print(chr(asci))