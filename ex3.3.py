import sys

def print_capacity(list):
    capacity = sys.getsizeof(list)-sys.getsizeof(list.__sizeof__)
    print("Capacity of List: ") + capacity

list = []
prev_capacity = 0
for number in range(64):
    list.append(number)
    if (prev_capacity != sys.getsizeof(list)):
        print_capacity(list)
        prev_capacity = sys.getsizeof(list)