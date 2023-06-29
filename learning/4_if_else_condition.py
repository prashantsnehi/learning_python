num = int(input("Please enter any number... "))

if num == 0:
    print(num, " is an even number")
elif num % 2 == 0:
    print(num, " is even number")
else:
    print(num, " is odd number")

marks = int(input("Enter the marks... "))
if 85 < marks <= 100:
    print("Congratulations! You have scored grade A")
elif 60 < marks <= 85:
    print("Congratulations! You have scored grade B+")
elif 40 < marks <= 60:
    print("Congratulations! You have scored grade B")
elif 30 < marks <= 40:
    print("Congratulations! You have scored grade C")
else:
    print("Sorry! You are fail...")


