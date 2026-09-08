#Creation and insertion and checking of key
student={}

student["name"]="Pyth"
student["age"]=21
student["branch"]="csai"
print(student)

if "name" in student:
    print("Exists")
else:
    print("Not Exists")


#Perform operations
marks = {
    "math": 85,
    "python": 92,
    "sql": 78
}


print(marks["python"])
marks["sql"]=88
marks["dsa"]= 95

if "java" in marks:
    print("Exists")
else:
    print("Not Exists")

print("\n")
print(marks)
del marks["math"]
print(marks)


#Frequncy of characters in a string
s = "programming"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for key , val in freq.items():
    if val==1:
        print(key)


#Arranging words based on first character
def arrange(words):
    groups={}

    for word in words:
        if word[0] not in groups:
            groups[word[0]]=[word]
        else:
            groups[word[0]].append(word)
    return groups



words=["apple",
"ant",
"banana",
"avocado",
"ball"]
print(arrange(words))





#Calculating total marks of students
def get_total(students):
    result={}
    for name in students:
        total = 0
        for mark in students[name]["marks"]:
            total += mark
        result[name]=total
    return result

students = {
    "Ankush": {
        "marks": [85, 92, 88],
        "branch": "CSE"
    },
    "Rahul": {
        "marks": [78, 81, 90],
        "branch": "ECE"
    }
}

print(get_total(students))


#Getting names of students in CSE branch
def get_cse_students(students):
    result = []

    for name in students:
        if students[name]["branch"] == "CSE":
            result.append(name)

    return result

students = {
    "Ankush": {
        "marks": [85, 92, 88],
        "branch": "CSE"
    },
    "Rahul": {
        "marks": [78, 81, 90],
        "branch": "ECE"
    }
}

print(get_cse_students(students))

