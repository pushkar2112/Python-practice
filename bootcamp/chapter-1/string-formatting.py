# String formatting 

# using .format()

name = 'Sam'
age = 17
ctry = 'India'

print('His name is {n}, his age is {a}, he is from {c}'.format(n='Sam',a=17,c='INDIA'))
print('His name is {n}, his age is {a}, he is from {c}'.format(n=name,a=age,c=ctry))
print('His name is {}, his age is {}, he is from {}'.format(name, age, ctry))

# using f-strings

print(f'His name is {name}, his age is {age}, he is from {ctry}')

#           to get string representation
print(f'His name is {name!r}, his age is {age}, he is from {ctry!r}')

# Float formatting
print('half of his age is {:.2f}'.format(age/2))
print('half of his age is {:.4f}'.format(age/2))