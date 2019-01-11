# In the code cell, assign to the variable regex a regular expression that's four characters long and matches every string in the list strings.

strings = ["data science", "big data", "metadata"]
regex = "data"

# we use the special character "." to indicate that any character can be put in its place.
strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

# We can use the caret symbol ("^") to match the beginning of a string, and the dollar sign ("$") to match the end of a string.
# "^a" will match all strings that start with "a".
# "a$" will match all strings that end with "a"

# Assign a regular expression that's seven characters long and matches every string in strings (except for bad_string) to the variable regex.

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"


import csv
file = open('test.csv', 'r')
post_with_headers = csv.reader(file)
posts = post_with_headers[1:]
print(posts)
