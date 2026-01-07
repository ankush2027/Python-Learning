#While loop

#1-10
i=1
while i <= 10:
    print(i)
    i+=1

#Even numbers
for i in range(1,21):
    if i%2 == 0:
        print(i)


#Multiplication table

number=int(input("Enter the number : "))

for i in range(1,11):
    print(number,"x",i,"=",number*i)



#break and continue

i=1
while i<=10:
    print(i)
    if i==7:
        break
    i+=1

print("\n")
for i in range(1,11):
    if i==7:
        continue
    print(i)


#Sum of numbers
number=int(input("Enter the number starting from 1 : "))
total=0
for i in range(1,number+1):
    total=total+i
print(total)


#Count the digits - method 1
number=input("Enter a number : ")
print(len(number))

#method 2
number=int(input("Enter a number : "))
count=0
while number > 0:
    count=count + 1
    number=number//10

print(count)


#Factorial
n=int(input("Enter a number : "))
number=n
fact=1
while number>0:
    fact=fact*number
    number=number-1
print("The factorial of",n,"is :",fact) 