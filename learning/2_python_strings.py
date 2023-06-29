str1 = "Hi Python"
str2 = 'Hi Python'
str3 = '''Hi Python'''
print("First  string: ", str1)
print("Second string: ", str2)
print("third  string: ", str3)


# code to show how we use docstrings in Python
def add(x, y):
    """This function adds two input values"""
    return x + y


# displaying the docstrings of the add function
print(add.__doc__)
