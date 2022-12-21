from Queues import Queue

fifo = Queue()
fifo.enqueue("First")
fifo.enqueue("Second")
fifo.enqueue("Third")

print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())
