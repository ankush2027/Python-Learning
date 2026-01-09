#Function basics

def greet():
    name=input("Hey there ! what's your name : ")
    print("Hello",name,"👋")

greet()


#Sqaure of a number
def square():
    number=int(input("Enter a number : "))
    sqr=number**2
    print("The square of",number,"is",sqr)

square()


#Even and odd
def is_even():
    number=int(input("Enter a number :"))
    if number%2==0:
        return True
    else:
        return False
    
is_even()


#Name
def full_name(first,last):
    print("Hello",first,last)

full_name("John","Wick")

#Understanding return
def demo():
    print("A")
    return "B"

demo()
print(demo()) #This will not return none because you have the return in function


#Controlled input loop
def read_numbers():
    total=0
    while True:
        number=int(input("Enter a number :"))
        if number==0:
            break
        if number < 0:
            continue
        total+=number
    return total
    
print(read_numbers())