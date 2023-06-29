def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)

    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for key, value in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += value
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44


# The network() function accepts a dictionary "servers" as a parameter.
def network(servers):
    # A string variable is initialized to hold the "result".
    result = ""

    # For each "hostname" (key) and "IP address" (value) in the "server" dictionary items...
    for hostname, IP_address in servers.items():
        # A string identifying the hostname and IP address for each server is added
        # to the "result" variable. The string .format() function and is used to plug
        # the hostname and IP_address variables into the designated {} placeholders
        # within the string.
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"

    # Return the "result" variable string.
    return result


# Call the "network" function with the dictionary.
print(network({"Domain Name Server": "8.8.8.8", "Gateway Server": "192.168.1.1", "Print Server": "192.168.1.33",
               "Mail Server": "192.168.1.190"}))

# Should print:
# The IP address of the Domain Name Server server is 8.8.8.8
# The IP address of the Gateway Server server is 192.168.1.1
# The IP address of the Print Server server is 192.168.1.33
# The IP address of the Mail Server server is 192.168.1.190

