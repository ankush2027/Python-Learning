#Lists 

#Using built in class
numbers=list()
numbers.extend([10,20,30])
print(numbers)


#User input
def store_numbers():
    store=list()
    for i in range(5):
        numbers=int(input("Enter 5 numbers :"))
        store.append(numbers)
    print(store)


#Sum without built-in sum()
numbers=[1,2,4,61,2]
sum=0
for i in numbers:
    sum+=i
print("The sum of list is",sum)



#Even numbers
nums=[1,3,4,6,78,83,2,4,5]
even=list()
for i in nums:
    if i%2==0:
        even.append(i)

print("Even numbers are\n",even)
print("Count of even number is:",len(even))



#Slicing basics
number=[1,2,4,5,7,8,65,4]
print(number[0:4])#first three
print(number[-2:])#last two
print(number[1:7])#middle elements



#Accessing nested lists
a=[1,3,4,5]
b=[2,3,4,5]
c=[a,b]
print(c)
#Inner lists access
print(c[1][2])
print(c[0][-1])



#Append and extend
random=[12,3,4,5,"What?",2.33]
random.append([1,"hi"])
print(random)

random.extend([1,3,"bye bye"])
print(random)
