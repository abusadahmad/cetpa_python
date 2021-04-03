nums = [1,2,3,4,5]
for num in nums:
    print(num)


nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('found!')
        break
    print(num)


nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('found!')
        continue
    print(num)

nums = [1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num, letter)


for i in range(10):
    print(i)

# start while loop here

x = 0
while x < 10:
    print(x)
    x += 1


# here is infite loop if we not make a condition

x = 0
while True:
    print(x)
    if x == 5:
        breakn
    x += 1