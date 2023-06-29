def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


input_seconds = 5000
result = convert_seconds(input_seconds)
hours, minutes, remaining_seconds = convert_seconds(input_seconds)
print(type(result))
print(f'Tuple: {result}')
print(f'{input_seconds} seconds is equal to {hours} hour {minutes} minutes and {remaining_seconds} seconds')


def sales_prices(item_and_price):
    # Initialize variables "item" and "price" as strings
    item = ""
    price = ""
    # Create a variable "item_or_price" to hold the result of the split.
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:

        # Check if the element is a number
        if x.isalpha():

            # If true, assign the element to the "item" string variable and add a space
            # for any item names containing multiple words, like "Winter fleece jacket".
            item += x + " "

        # Else, if x is a number (if x.isalpha() is false):
        else:
            # Assign the element to the "price" string variable.
            price = x

    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence
    return "{} are on sale for ${}".format(item, price)


# Call to the function
print(sales_prices("Winter fleece jackets 49.99"))


# Should print "Winter fleece jackets are on sale for $49.99"


# This function accepts two variables, each containing a list of years.
# A current "recent_first" list contains [2022, 2018, 2011, 2006].
# An older "recent_last" list contains [1989, 1992, 1997, 2001].
# The lists need to be combined with the years in chronological order.
def record_profit_years(recent_first, recent_last):
    # Reverse the order of the "recent_first" list so that it is in
    # chronological order.
    recent_first.reverse()

    # Extend the "recent_last" list by appending the newly reversed
    # "recent_first" list.
    recent_last.extend(recent_first)

    # Return the "recent_last", which now contains the two lists
    # combined in chronological order.
    return recent_last


# Assign the two lists to the two variables to be passed to the
# record_profit_years() function.
recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

# Call the record_profit_years() function and pass the two lists as
# parameters.
print(record_profit_years(recent_first, recent_last))


# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]


# The function accepts two parameters: a start year and an end year.
def list_years(start, end):
    # It returns a list comprehension that creates a list of years in a for
    # loop using a range from the start year to the end year (inclusive of
    # the upper range year, using end+1).
    return [year for year in range(start, end + 1)]


# Call the years() function with two parameters.
print(list_years(1972, 1975))


# Should print [1972, 1973, 1974, 1975]


# The function accepts two variable integers through the parameters and
# returns all odd numbers between x and y-1.
def odd_numbers(x, y):
    # This list comprehension uses a for loop to iterate through values
    # of n in a range from x to y, with the value of y excluded (meaning
    # keep the default range() function behavior to exclude the
    # end-of-range value from the range). Since an incremental value is not
    # specified, the range function uses the default increment of +1.
    # The if condition checks n to test if the number is odd using the
    # modulo operator. This condition is written to check if n is divided
    # by 2, that the remainder is not 0.
    return [n for n in range(x, y) if n % 2 != 0]


# Call the years() function with two parameters.
print(odd_numbers(5, 15))
# Should print [5, 7, 9, 11, 13]
