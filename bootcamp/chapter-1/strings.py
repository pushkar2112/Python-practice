# Strings are used in Python to record text information, such as names.
# Strings in Python are actually a sequence, which basically means Python keeps track 
# of every element in the string as a sequence. 
# For example, Python understands the string "hello' to be a sequence of letters in a specific order. 
# This means we will be able to use indexing to grab particular letters 
# (like the first letter, or the last letter).


s1 = 'hello'
s2 = "This is a sample string"

print('This is another sample string')
print('it"s an example to show how to use a quote in a quote')

# len function on string
print(len(s2))

#                        string sllicing
# string indexes starts from 0 when going left to right
# -1 from right
# [start:stop:step]

print(s2[5::])

# STRING PROPERTIES
#It's important to note that strings have an important property known as immutability.
# This means that once a string is created, the elements within it can not be changed or replaced.


# String Concatenation
print(s1 + s2)

# REPITITION
print(s1 * 5)

# Built-in Methods
cap = 'HELLO PEOPLE'

print(cap.lower())
cap = cap.lower()
print(cap.upper())

print(cap.split())
print(cap.split('h'))

#String formatting
print('this is sample formatting and {}'.format(s2))