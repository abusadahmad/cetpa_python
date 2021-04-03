def hello_func():
    pass
print(hello_func())


def hello_func():
    print('Hello Function')
hello_func()


def hello_func():
    return 'Hello function'
print(hello_func().upper())     # here we can use all string method here


def hello_func(greeting):
    return '{} function'.format(greeting)
print(hello_func('Hi'))     # here we can use all string method here


def hello_func(greeting, name='you'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi', name='Corey'))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('math', 'arts', name='john', age=21)

