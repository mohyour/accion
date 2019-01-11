# List comprehension

my_list = [1,2,3,4,5] # [2,4,6,8,10]

# tradional for loop
my_list2 = []
for i in my_list:
  my_list2.append(i*2)

print(my_list2)

#list comprehension
my_list2 = [i*2 for i in my_list]
print(my_list2)

list_of_list = [[1,2], [3,4], [5,6]]
result = []
for i in list_of_list:
  new_list = []
  for x in i:
    new_list.append(x*2)
  result.append(new_list)

print(result)

#comprehension
result = [[x*2 for x in i] for i in list_of_list ]
print(result)

