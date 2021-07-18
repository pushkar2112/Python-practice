# open a new file
f = open('C:\\Users\\Pushkar\\repos\\Python-practice\\bootcamp\\chapter-1\\sample-text-file.txt')
#f = open('sample-text-file.txt')    #not working... why?

#read file
val = f.read()
print(val)

# after reading the file the pointer reaches the end position in the file
# seek is used to move the pointer and tell is used to get the ccurrent position of the cursor(pointer)

fend = f.read()
print('--- ',fend,' ---')        # prints nothing

f.seek(0)
print(f.read())
print(f.tell())

# reading methods- they load the entire file in the memory
# read()- reads the whole file
# readline(-line number-)- reads the line whose position is passed
# readlines()- returns the list of all the lines in a file

f.seek(0)
print(f.readlines())

# It is a good practise to always close the file
f.close()