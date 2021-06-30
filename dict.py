# int(‘10’) + 1  (Converts a string with has ‘10’ as the
# data into an integer and adds 1)
# int_1 = int(String1) + 10  (Converts String
# to binary, adds 10, and sets int_1 to the value)

# random sales dictionary
sales = {'apple': 3, 'orange': 4, 'grapes': 5}
sales1 = {'Apple': 6, 'Orange': 8, 'Grapes': 10}

sales.update(sales1)
print(sales)
