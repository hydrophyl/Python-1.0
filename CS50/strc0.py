from cs50 import get_string

students = []

for i in range(3):
    name = get_string("Your Name: ")
    dorm = get_string("Your Dorm: ")

    student = {"name": name, "dorm": dorm}
    
    students.append(student)
for student in students:
    print(f"{student['name']} is in Dorm {student['dorm']}")