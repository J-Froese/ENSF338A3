import json
import matplotlib.pyplot as plt
import urllib.request
import time

# load the array and search tasks from URLs
with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json') as f:
    data = json.loads(f.read().decode())
    data_arr = data
with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json') as f:
    all_tasks = json.loads(f.read().decode())

# binary search function with initial mid point configured
def binary_search(arr, target, start, end, initial_mid):
    mid = initial_mid
    while start <= end:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return -1

# time performance for each task
results = []
for task in all_tasks:
    start = 0
    end = len(data_arr) - 1
    best_mid = -1
    best_time = float('inf')
    for mid in range(start, end + 1):
        t0 = time.time()
        binary_search(data_arr, task, start, end, mid)
        t1 = time.time()
        elapsed_time = t1 - t0
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_mid = mid
    results.append((task, best_mid))

# scatter plots for search tasks
x = [task for task, _ in results]
y = [mid for _, mid in results]

print(x)
print(y)

plt.scatter(x, y)
plt.xlabel('Search Task')
plt.ylabel('Initial Midpoint')
plt.title('Binary Search Initial Midpoint Optimization')
plt.show()
