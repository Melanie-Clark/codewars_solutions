"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list
with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]

"""

def filter_list(l: list) -> list:
    new_list = []
    for i in l:
        if type(i) != str:
            new_list.append(i)
    return new_list


# list comprehension
def filter_list(l: list) -> list:
    return [i for i in l if type(i) != str]

print(filter_list([1, 2, 'a', 'b']))