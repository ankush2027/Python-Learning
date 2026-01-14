# #Dictionaries

# #1
# user = {
#     "name":"Messi",
#     "email":"goat10@gmail.com",
#     "age":37,
#     "is_verified":False
# }

# print(user["email"])

# #2
# user = {
#     "name":"Messi",
#     "email":"goat10@gmail.com",
#     "age":37,
#     "is_verified":False
# }

# print(user["email"])

# for key,value in user.items():
#     print(key,":",value)


# #Printing !present key
# data = {"x": 10}
# print(data.get("y")) 


#Updating values
user = {"name": "A", "age": 20}
if "age" in user:
    user["age"]+=1
else:
    user["age"]=1

print(user)


# #Looping
# data = {"a": 1, "b": 2, "c": 3}
# for key,value in data.items():
#     print(key,"->",value)



# #Creating dictionary

# data1={"a":1,"b":2}
# print(data1)
# print("\n")
# data2=dict(a=1,b=2)
# print(data2)



