print("Hello_world")
print("Bobby's Tylor")
print('Music\s collection')

message = "Hello world"
print(message)

print(len(message))
print(message[0])
print(message[0:6])
print(message[5:])
print(message[:6])
print(message.count('l'))
print(message.find('world'))

new_message = message.replace('world','universe')
print(new_message)

greeting = 'Hello'
name = 'John'
messages = '{},{}.welcome'.format(greeting,name)
print(messages)

print(dir(name))

print(help(str.lower))
