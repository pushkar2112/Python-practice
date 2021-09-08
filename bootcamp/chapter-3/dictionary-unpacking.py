
# Iterrating through a dictionary produces only the keys
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

# To get the values
for value in d.values():
    print(value)

# To get the key value pairs in a list
items = d.items()

for k,v in items:
    print(k)
    print(v)

# REMEMBER- Dictionaries are unordered 
print(sorted(d.values()))