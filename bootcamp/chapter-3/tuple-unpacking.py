# Tuples have a special quality when it comes to for loops.
# If you are iterating through a sequence that contains tuples
# the item can actually be the tuple itself, this is an example of tuple unpacking.
# During the for loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!

list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)

# Now with unpacking!
for (t1,t2) in list2:
    print(t1)