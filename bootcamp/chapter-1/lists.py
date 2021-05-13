# Lists can be thought of the most general version of a sequence in Python. 
# Unlike strings, they are mutable, meaning the elements inside a list can be changed!

mylist = ['hello', 21, 3.14, [1,2,3,'world']]

print(len(mylist))

# List methods

sl = [21,12,'sam']

sl.append('joe')

popped_item = sl.pop(1)

print(popped_item)
print(sl)

sl = [1,85,14,21,65,18,11,10,5]

sl.sort()
print(sl)

sl.reverse()
print(sl)