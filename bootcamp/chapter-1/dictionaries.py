# A colection of key value pairs
# Keys need to be a string

my_dict = {'name':'john', 'age':27, 'gender':'male', 'subs': ['Eng', 'Math', 'Sci'], 'marks':(58, 79,63)}
print(my_dict['name'])

print(my_dict['age'])
my_dict['age'] += 3
print(my_dict['age'])

print(my_dict['subs'])
print(my_dict['marks'])

print(my_dict['subs'][1],end='--')
print(my_dict['marks'][1])

# Other ways to make a dictionary
d = {}
d['key1'] = 'value1'
d['key2'] = 'value2'

print(d)


# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])

# DIctionary methods

d = {'key1':1, 'key2':2}
print(d.keys())
print(d.values())
print(d.items())