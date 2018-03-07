from BoundedQueue import BoundedQueue
from CircularQueue import CircularQueue
import time
def main():
    b = BoundedQueue(10000)
    c = CircularQueue(10000)
    for i in range(10000):
        b.enqueue(i)
        c.enqueue(i)
    start1=time.time()
    for i in range(10000):
        b.dequeue()
    print("BoundedQueue running time is:",time.time()-start1)
    start2=time.time()
    for i in range(10000):
        c.dequeue()
    print("CircularQueue running time is:",time.time()-start2)
main()