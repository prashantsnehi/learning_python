# num = [34, 12, 54, 23, 75, 34, 11, 7]


# using function to get prime number
def prime_number(number) -> object:
    condition = 0
    iteration = 2
    while iteration <= number / 2:
        if number % iteration == 0:
            condition = 1
            break
        iteration = iteration + 1

    if condition == 0:
        print(f"{number} is PRIME number")
    else:
        print(f"{number} is not a PRIME number")


for i in range(100):
    prime_number(i)
