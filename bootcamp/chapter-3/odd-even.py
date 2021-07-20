
# Initialising a list of 10 nos.
list1 = range(1,11)

# To print all the even nos. from a list
print('EVEN')
for num in list1:
    if num % 2 == 0:
        print(num)

# To print all the odd nos. from a list
print('\nODD')
for num in list1:
    if num % 2 != 0:
        print(num)

# ALTERNATE Using List comprehension
even = [i for i in list1 if i%2 == 0]
print('Even', even) # Readability is the PRIORITY
    
odd = [i for i in list1 if i%2 != 0]
print('Oddṇ', odd)