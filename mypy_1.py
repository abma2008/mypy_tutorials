'''
This First Tutorial we will be introducing how to define the variables using typing hints.
It should be a straight-forward lesson...
please be aware of the syntax...

'''

# defining a variable with string type:
value_string: str = 'I am a string type hint'
# defining a variable with integer type:
value_integer: int = 10
# definig a variable with float type:
value_float: float = 10.5
# defining a varialble with list type and specify what type hint it should contain:
value_list: list[str] = ['Hello', 'world']
# defining a variable with dict type and specifying what the key and vcalue should contain:
value_dict: dict[str, int] = {'Hello': 1, 'world': 2}
# defining a variable with tuple type and specifying what it should contain:
value_tuple: tuple[str]=('hello',)
# defining a variable with set type and specifying what it should contain:
value_set: set[str | int] = {1, 'hello', 2, 'world'}


'''
Type hints are useful during writing the code, which means they can alertify you if
there is a mis-type match during writing the code.
But Python is a dynamic language where the type is checked during the execution time.
But if you use mypy, it can detect if everything is wrong fine according to your specification
or it raises an error and displays the message for it.
'''
