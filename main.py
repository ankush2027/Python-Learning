import csv
import json

cleaned_data = []
filtered_data = []
ages = []

with open('users.csv') as file:
    file_reader = csv.DictReader(file)

    for row in file_reader:
        if row["name"] and row["signup_date"]:
            filtered_data.append(row)

for row in filtered_data:
    if row["age"]:
        ages.append(int(row["age"]))

average_age = int(sum(ages) / len(ages))

for row in filtered_data:
    if row["age"] == '':
        row["age"] = str(average_age)

for row in filtered_data:
    if "@" in row["email"] and "." in row["email"]:
        cleaned_data.append(row)

print(cleaned_data)


fieldnames = cleaned_data[0].keys()

with open("clean_users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

with open("clean_users.json","w") as file:
    json.dump(cleaned_data, file, indent=4)

