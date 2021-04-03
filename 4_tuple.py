# MUTABLE
list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0]='Art'
print(list_2)
print(list_1)

# IMMUTABLE
list_1 = ('History','Math','Physics','CompSci')
list_2 = list_1
print(list_1)
print(list_2)

list_1[0]='Education'       # can't change the value becuase it's immutable
print(list_1)
print(list_2)
