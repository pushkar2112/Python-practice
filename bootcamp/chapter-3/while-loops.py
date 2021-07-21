#A while statement will repeatedly execute a single statement or group of statements as long as the condition is true. 
# The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.

# Example
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print('All Done!')

# BREAK, CONTINUE, PASS
'''
break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all.'''

# Example
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue