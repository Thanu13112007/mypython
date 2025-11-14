#dictionary
student={
    "name" :"thanu",
    "age"  :18,
    "roll" :44
}
print(student)
student["dob"]=13.11
print(student)
del student["dob"]
print(student)
for i in student:
  print(i,student)
{'name': 'thanu', 'age': 18, 'roll': 44}
{'name': 'thanu', 'age': 18, 'roll': 44, 'dob': 13.11}
{'name': 'thanu', 'age': 18, 'roll': 44}
name {'name': 'thanu', 'age': 18, 'roll': 44}
age {'name': 'thanu', 'age': 18, 'roll': 44}
roll {'name': 'thanu', 'age': 18, 'roll': 44}
