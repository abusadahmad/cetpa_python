student = {'name':'John','age':34,'courses':['Math','Physics']}
print(student)

print(student['name'])
print(student.get('name'))

#print(student['phone']='0551320')
#print(student['name']='James')

#print(student.update{'name':'James','age':23,'phone':'0551320'})


del student['age']
age = student.pop('age')
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key,value in student item():
    print(key,value)