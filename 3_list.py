courses = ['History','Math','Physics','CompSci']
print(courses)

print(len(courses))
print(courses[1])
print(courses[-1])
print(courses[0:2])

courses.append('Art')
print(courses)

courses.insert(0, 'English')
print(courses)

print(courses.index('CompSci'))
print('Art' in courses)

courses_2 = ['Education','Economics']
courses.insert(0, courses_2)
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('Math')
print(courses)

popped = courses.pop()
print(popped)

num = [1,5,4,3,6,7]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(min(num))
print(max(num))
print(sum(num))
