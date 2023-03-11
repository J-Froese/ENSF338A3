import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        # Implement enqueue function
        while True:
            n = None
            self.lock()
            n = self.queue[self.tail]
            if n==None:
                self.queue[self.tail] = data
                if self.tail+1==self.size:
                    self.tail=0
                else:
                    self.tail=self.tail+1
                self.unlock()
                return
            self.unlock()
            time.sleep(1)
    
    def dequeue(self):
        # Implement dequeue function
        while True:
            n = None
            self.lock()
            n = self.queue[self.head]
            if n!=None:
                self.queue[self.head] = None
                if self.head+1==self.size:
                    self.head=0
                else:
                    self.head=self.head+1
                self.unlock()
                return n
            self.unlock()
            time.sleep(1)


def producer():
    while True:
        # Implement producer function
        i = random.randint(1,10)
        time.sleep(i)
        q.enqueue(i)

def consumer():
    while True:
        # Implement consumer function
        i = random.randint(1,10)
        time.sleep(i)
        n = q.dequeue()
        print(n)

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
