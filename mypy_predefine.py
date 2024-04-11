'''
Trying to predefine variables without making initial value....
hopefully, this one will work.

'''

# defining a dictionary without specifying its key and values:
mydict: dict[str, int] = dict()

# trying to add values into mydict:
mydict['Hello World'] = 1
# adding an invalid key and value:
mydict ['hello world 2'] = 2