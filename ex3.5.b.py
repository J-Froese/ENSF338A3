import heapq
import random
import timeit
import matplotlib.pyplot as plt

#inefficient implementation
class PriorityQueue:
    def __init__(self):
        self._queue = []
        
    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, item))
        
    def remove(self):
        return heapq.heappop(self._queue)[1]

#efficient implementation
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        
    def insert(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        
    def remove(self):
        return heapq.heappop(self._queue)[-1]
       

def inefficient():
    pq = PriorityQueue()
    for x in range(1000):
        pq.insert(x, random.randint(0, 1000))
        pq.remove()

def efficient():
    pq = PriorityQueue()
    for y in range(1000):
        pq.insert(y, random.randint(0, 1000))
        pq.remove()

times_ineff = []
times_eff = []

for x in range(100):
    times_ineff.append(timeit.timeit(inefficient, number=100))
    times_eff.append(timeit.timeit(inefficient, number=100))


#Plot distribution of values
plt.hist(times_ineff, bins=20, alpha=0.6, label='Inefficient')
plt.hist(times_eff, bins=20, alpha=0.6, label='Efficient')
plt.legend(loc='upper left')
plt.show()

print("Inefficient ","min:", min(times_ineff),"max:", max(times_ineff),"sum:", sum(times_ineff)/len(times_ineff))
print("Efficient ", "min:", min(times_eff),"max:", max(times_eff),"sum:", sum(times_eff)/len(times_eff))

