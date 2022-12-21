from Queues import Queue

fifo = Queue("First", "Second", "Third")
print(len(fifo))
for element in fifo:
    print(element)
print(len(fifo))

