#Lists and loops 


#Filtering positive lists
nums = [3, -1, 0, 7, -5, 8]
pos = []
for n in nums:
    if n > 0:
        pos.append(n)
print(pos)


#Count 
nums = [3, -1, 0, 7, -5, 8]
multiples=[]
for n in nums:
    if n % 10 == 0:
        multiples.append(n)
print("The length of multiples is",len(multiples))
        

#User Input 
numbers=[]
while True:
    user=int(input("Enter a number : "))
    if user == 0:
        break
    else:
        numbers.append(user)
print(numbers)



#Separate lists
nums=[1,3,4,9,221,23,44,11]
even=[]
odd=[]
for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Even numbers \n",even)
print("Odd numbers \n",odd)


#Slicing
a = [5, 10, 15, 20, 25, 30]
print(a[2:5])
print(a[2:])
print(a[-3:])


#Nested logic
data = [[1, 2], [3, 4], [5, 6]]
total=0
for num in data:
    for n in num:
        total+=n
print(total)