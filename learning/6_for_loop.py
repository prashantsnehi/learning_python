print(range(0, 15))

print(list(range(15)))

print(list(range(4, 9)))

print(list(range(5, 25, 4)))

# Python program to iterate over a sequence with the help of indexing
tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")

# iterating over tuple_ using range() function
for iterator in range(len(tuple_)):
    print(tuple_[iterator].upper())

# using continue statement
# continue statement
for string in "Python strings in loop":
    if string == "a" or string == "e" or string == "i" or string == "o" or string == "u" or string == " ":
        continue

    print("Current letter is... ", string)

# break statement
for string in "Python strings in loop":
    if string == "l":
        break
    elif string == " ":
        continue
    print("Current letter is... ", string)

# pass statement: Pass statements are used to create empty loops. Pass statement is also employed for classes,
# functions, and empty control statements.

for string in "Python strings in loop":
    pass

print("Last letter in string is... ", string, end='\n')

