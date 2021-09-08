# RANGE
# The range function allows you to quickly generate a list of integers
#range(start, stop, step)

print(list(range(0,101,10)))

# ENUMERATE
# Enumerate was created to keep track of how many loops you've gone through

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter)) # Tuple unpacking

# ZIP
# To zip two lists together

print(list(enumerate('abcde'))) # Enumerate returns tuples

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

for item1, item2 in zip(mylist1,mylist2): # Zip is a generator, thus accessed only in a loop
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

# MIN MAX
print(min(mylist1))
print(max(mylist1))

# RANDOM
# randint - includes the start and stop
# random.shuffle - This shuffles the list "in-place" meaning it won't return anything, 
# instead it will effect the list passed

from random import shuffle
print(shuffle(mylist1))

from random import randint
print(randint(1, 10))