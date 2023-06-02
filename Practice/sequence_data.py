###
# Sequence Data Types Exercise
# Author: Nam Jun Lee
# Date: Sept 9th, 2021
###

# 10 unique elements in the range
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 10 random elements between 5 and 20
list_2 = [6, 7, 9, 13, 18, 8, 10, 12, 19, 15]

# List with elements combined from list_1 and list_2
comb_list = list_1 + list_2
print(comb_list)

# Dictionary mapping each elements of list_1 with corresponding element of list_2
dict_list = dict(zip(list_1, list_2))
print(dict_list)

# Tuple with combined values of list_1 and list_2
comb_tuple = tuple(comb_list)
print(comb_tuple)

# Set with all uniques values of list_1 and list_2
comb_set = set(comb_list)
print(comb_set)
