def get_table(number):
    counter = 1
    # we will use a while loop for iterating 10 times for the multiplication table
    while counter <= 10:  # specifying the condition
        ans = number * counter
        print(f"{number} X {counter} = {ans}")
        counter = counter + 1  # expression to increment the counter


# calling the function based on input from user
num = int(input("Please enter any number to get table: "))

get_table(num)
