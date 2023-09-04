# Function for unknown list of arguments
def printlist(*args):
    for i in args:
        print(i)

printlist(1,2,3,4,5)

# Dictionary function
def printlist1(**dict):
    print(dict)

printlist1(name = 'messi', age = 30, position = 'forward')