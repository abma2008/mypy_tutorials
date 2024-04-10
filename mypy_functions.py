'''
This is the part where we use typing hints inside a function of python.
As I said, learning how to implement hints on python can play a major 
role in the future since there is a possibility of it shifting there
because static typing languages are more faster than dynamic typing
languages.
please view the following lesson and practice

'''
# defining a basic function with typing hints:
def addition(v1: int, v2: int) -> int:
    return v1 + v2

# -> int is specifying that the function should return a type int as a result of its execution:
print(f'the result of addition:{addition(10,3)}')

# defining another function:
def subtraction(v1: float, v2: float) -> float:
    return v1 - v2
print(f'the result of subtraction: {subtraction(10,3)}')

# defining another function:
def fullname(first: str, last: str) -> str:
    return f'{first} {last}'
print(f'Your name is: {fullname('ahmed','saeed')}')

'''
This is a simple typing hints on a function:
but be aware that during execution, the type hints are of not effect at all.
because Python is a dynamic language, which means the checking of a type can
only be done during execution.
'''