# Python program to show how to use a while loop
counter = 0

# initiate the loop
while counter < 10:  # giving the condition
    counter = counter + 1
    print(counter, "Python while loop")

# Python program to show how to use else statement with the while loop
counter = 0
while counter < 10:
    counter = counter + 1
    print("Python loops")  # Executed until condition is met
# Once the condition of while loop gives False this statement will be executed
else:
    print("Code block inside the else statement")

# Python program to show how to write a single statement while loop
counter = 0

while counter < 10:
    counter = counter + 1
    if counter % 2 == 0:
        continue
    # print(counter, " is even number")
    else:
        print(counter, " is odd number")

