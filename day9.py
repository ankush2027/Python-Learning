#Sets

#Deduplication
nums=[1,2,3,3,4,4,3,22,4,2,3,212,21,1]
print(list(set(nums)))


#Membership check
user_input=int(input("Enter a number : "))
allowed={1,2,3,4,5,66,7,8}
if user_input in allowed:
    print("Allowed")
else:
    print("Not Allowed")



#Intersection
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"Intersection elements : {a&b}")
print(a-b)
print(b-a)



#Type behaviour
s = {1, True, 1.0, False, 0} #1=True=1.0 has same hash and also for false and 0 same hash so it considers as single
print(s)



#Set update
permissions = {"read"}
permissions.add("write")
permissions.add("delete")
print(permissions)
permissions.discard("read")
print(permissions)


