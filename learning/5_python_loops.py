# while loop: Repeats a statement or group of statements while a given condition is TRUE. It tests the condition
# before executing the loop body.

# loop control statements break continue pass
# python program to show how loop works
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]

print("Original numbers...", numbers)
# variable to store the square of the number
square = 0

# creating an empty string
squares = []

# creating loop
for value in numbers:
    square = value ** 2
    squares.append(square)

print("The list of squares is... ", squares)

# Python program to show how if-else statements work
string = "python string"
for char in string:
    # giving a condition in if block
    if char == "o":
        print("in the if block...")
    # if condition is not satisfied then else block will be executed
    else:
        print("Out of if block...", char)

# Python program to show how to use else statement with for loop

# Creating a sequence
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)
# Initiating the loop
for value in tuple_:
    if value % 2 != 0:
        print(value)
# giving an else statement
else:
    print("These are odd number in tuple")

# for loop: This type of loop executes a code block multiple times and abbreviates the code that manages the loop
# variable.

# nested loops: We can iterate a loop inside another loop.

