# Create a dictionary and apply the following methods:
# Print the dictionary items, Access items, Use get(), Change values, Use len()

# create a dictionary
student = {
    "name" : "Rahul",
    "course" : "MCA",
    "semester" : 3,
    "marks" : 85,
}

# 1. print the dictionary items
print("Dictionary :",student)

# 2. Access items
print("Student Name :",student["name"])
print("Student Name :",student["course"])

# 3. Use get()
print("Semester :", student.get("semester"))
print("Maths :", student.get("marks"))

# 4. Change values
student["marks"] = 90
student["semester"] = 4

print("Dictionary after changing values :", student)

# 5. Use len()
print("Number of items :",len(student))