# Tuples are immutable

t = ('Sam', 'Andy', 25, 21, 54.021, 21)
# We can perform Indexing, Slicing

# Tuple Methods
print(t.index('Sam'))
print(t.count(21))

# Sets are a collection of unique values

my_set = set(t)
print(my_set)

my_set.add(22)  # to add new values to a set
print(my_set)
