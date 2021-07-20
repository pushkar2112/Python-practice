# Example of If Elif and Else statements
# They can be nested

loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')

#  for loop acts as an iterator in Python
#  it goes through items that are in a sequence or any other iterable item.

# Iterating through a list
list1 = range(1,11)
for num in list1:
    print(num)