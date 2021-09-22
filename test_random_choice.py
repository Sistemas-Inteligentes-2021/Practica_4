import random
from numpy.random import choice

# List Integers 
sample_list = [100, 200, 300, 400, 500]
sample_weights = [10, 20, 30, 40, 50]
sample_weights2 = [0.1, 0.2, 0.3, 0.2, 0.2] # Sum = 1


# List Strings 
my_list = ['manzana', 'banana', 'pera', 'uva']
my_weights = [0.2, 0.3, 0.1, 0.4]

super_test = [i[0] for i in my_list ]
print(super_test)
# List Strings 
elements = ['one', 'two', 'three'] 
weights = [0.2, 0.3, 0.5]

# Choices
random_list = random.choices(sample_list, weights=sample_weights, k=2)
random_list2 = random.choices(my_list, weights=my_weights, k=2)

# Choice
random_list3 = choice(sample_list, p=sample_weights2)
random_list4 = choice(my_list, p=my_weights)

# print(random_list)
# print(random_list2)
print(random_list3)
print(random_list4)