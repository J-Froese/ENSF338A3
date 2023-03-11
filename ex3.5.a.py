import matplotlib.pyplot as plt
import timeit
import random


#The code below is for the inefficient implementation
def linear(array, target_value):
    for x in range(len(array)):
        if array[x] == target_value:
            return x
    return -1

#The code below is for the efficient implementation
def binary(array, target_value):
    left = 0
    right = len(array) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if(array[midpoint] == target_value):
            return midpoint
        elif array[midpoint] < target_value:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return -1

linear_results = []
binary_results = []

for x in range(100):
    array = sorted([random.randint(1, 1000) for el in range(1000)])
    target_value = random.randint(1, 1000)
    linear_results.append(timeit.timeit(lambda: linear(array, target_value), number=100))
    binary_results.append(timeit.timeit(lambda: binary(array, target_value), number=100))

plt.hist(linear_results, alpha=0.75, label='linear search')
plt.hist(binary_results, alpha=0.75, label='binary search')
plt.legend(loc='upper left')
plt.show()

length_results_binary = len(binary_results)
length_results_linear = len(linear_results)

print('Average execution time for the linear search: ', sum(linear_results)/length_results_linear)
print('Average execution time for binary search: ', sum(binary_results)/length_results_binary)
