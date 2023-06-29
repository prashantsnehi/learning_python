import string

# print(f'ascii lowercase letters: {string.ascii_lowercase}')
# print(f'ascii uppercase letters: {string.ascii_uppercase}')
# print(f'string.digits: {string.digits}')
# print(f'string.hexadigits: {string.hexdigits}')
# print(f'string.octadigits: {string.octdigits}')
# print(f'string.punctuactions: {string.punctuation}')

my_list = ["The", "Quick", "Brown", "Fox", "Jumps", "Over", "The", "Little", "Lazy", "Dog"]
new_string = ""
for word in my_list:
    new_string += word + " "

print(my_list)
print(new_string)


def fahrenheit_to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 100, 10):
    print("{:<3} F | {:>6.2f} C".format(x, fahrenheit_to_celsius(x)))

