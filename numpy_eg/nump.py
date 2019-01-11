# Numpy - Data quest
# numpy ndarray documentation - https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.ndarray.html

import numpy as np # as allows us to import numpy module using another name
import csv # using python's inbuilt csv module to import our csv file
# our list of lists is stored as data_list

#import nyc_taxi.csv as a list of lists
f = open("taxi.csv", "r")
taxi_list = list(csv.reader(f))
taxi_list = taxi_list[1:] #remove header row
# print(taxi_list)

# convert all value to float
converted_list = [[float(x) for x in row] for row in taxi_list]

# converted_list = []
# for row in taxi_list:
#     converted = []
#     for x in row:
#         converted.append(float(x))
#     converted_list.append(converted)

# convert taxi_list to numpy array - returns a tuple of rows and column
taxi_ndarray = np.array(converted_list)
# print(type(taxi_ndarray))

#array.shape lets us see how many rows and column a numpy array has
# print(taxi_ndarray.shape)

# select a row in ndarray
# ndarray[row,column] or ndarray[row]
# Where row defines the location along the row axis and column defines the location along the column axis. Both row and column can be one of the following:

# An integer, indicating a specific location, eg ndarray[3,0].
# A slice, indicating a range of locations, eg ndarray[0:5,6:].
# A colon, indicating every location, eg ndarray[:,2].
# A list of values, indicating specific locations, eg ndarray[[0,1,3,4],0].
# A boolean array, indicating specific locations

# print(taxi_ndarray[3, 0])
# print(taxi_ndarray[0:5, 6])
# print(taxi_ndarray[:,3])
# print(taxi_ndarray[:,4:9])
# print(taxi_ndarray[:,[1,3,8]])

# print(taxi_ndarray[0:4,0])

# Operations on numpy vectors
# vector_a + vector_b - Addition
# vector_a - vector_b - Subtraction
# vector_a * vector_b - Multiplication (this is unrelated to the vector multiplication used in linear algebra).
# vector_a / vector_b - Division
# vector_a % vector_b - Modulus (find the remainder when vector_a is divided by vector_b)
# vector_a ** vector_b - Exponent (raise vector_a to the power of vector_b)
# vector_a // vector_b - Floor Division (divide vector_a by vector_b, rounding down to the nearest integer)

# Calculating miles per hour using the trip distance and the trip_length - miles per hour = distance in miles / length in hours

distance = taxi_ndarray[:, 7] # selects all rows at column 7
trip_length_in_secs = taxi_ndarray[:, 8]
trip_length_in_hours =  trip_length_in_secs / 3600 # converts all rows to hours
# using the `/` operator:
trip_mph_1 = distance / trip_length_in_hours

# using numpy - more at https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.math.html#arithmetic-operations
trip_mph_2 = np.divide(distance, trip_length_in_hours)

# Numpy ndarrays have methods for many different calculations. A few key methods are:
# ndarray.min() to calculate the minimum value - taxi_ndarray.min() or np.min(taxi_ndarray)
# ndarray.max() to calculate the maximum value
# ndarray.mean() to calculate the mean average value
# ndarray.sum() to calculate the sum of the values

min_value = trip_mph_2.min()
# stats for ndarray return one value - max in all elements in the ndarray
min_val = taxi_ndarray.min()
# find stats value along row - axis = 1, along column: axis = 0
max_val = taxi_ndarray.max(axis=0)
print(max_val)



my_list = [[1,2], [3.4], [5,6]]

result = []
for num in my_list:
    mult = []
    for i in num:
        mult.append(i*2)
    result.append(mult)

print(result)
