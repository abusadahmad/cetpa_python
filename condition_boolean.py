if True:
    print('condition is true')

language = 'python'
if language == 'python':
    print('language is python')
else:
    print('no match')

language = 'java'
if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
else:
    print('no match')

# and or & not operation
user = 'Admin'
password = False

if user == 'Admin' and password:
    print('welcome to admin page')
else:
    print('bad creds')


user = 'Admin'
password = True

if user == 'Admin' or password:
    print('welcome to admin page')
else:
    print('bad creds')


user = 'Admin'
password = False

if not password:
    print('please log in ')
else:
    print('welcome')


# if we not pass any value from condition it will be false else True
condition = None
if condition:
    print('evaluate to true')
else:
    print('evaluate to false')
