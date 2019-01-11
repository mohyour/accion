# Opening Files

# To open a file in Python, we use the open() function. This function accepts two different arguments (inputs) in the parentheses, always in the following order:
# * the name of the file (as a string)
# * the mode of working with the file (as a string)

# a = open("test.csv", "r")
# print(a)

# We use the read() function to read the contents of "test.txt"

# data = a.read()
# print(data)
# a.close()

with open("test.csv", "r") as a:
    data = a.read()
# Split file content into array
splitted_data = data.split('\n')
# print(splitted_data)

# split each column
data_list = []
for line in splitted_data:
    data_list.append(line.split(','))
# print(data_list)

movie_id = []
movie_name = []
for data in data_list[:len(data_list)-1]:
    movie_id.append(int(data[0]))
    movie_name.append(data[1])

# print(movie_id)
# print(movie_name)

print(sum(movie_id)/len(movie_id))
