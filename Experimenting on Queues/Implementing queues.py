from Queues import Queue
from Queues import Stack
from heapq import heappush
from Queues import PriorityQueue



#This is for First-In, First-Out Queue
print("======================Queues=================================")
fifo = Queue("First", "Second", "Third")
print(len(fifo))
for element in fifo:
    print(element)
print(len(fifo))
print("======================Stacks===================================")
#This is for Stacks
lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
    print(element)

print()
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop())
print(lifo.pop())
print(lifo.pop())

print("======================headppush===================================")
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")
print(fruits)

print("======================Tuple Comparison===================================")
Student1 = ("Mark", "Brown", 24)
Student2 = ("Stephen", "Parks", 42)
Student3 = ("Iron", "Man", 24)

print(Student1 > Student3)
print(Student2 < Student3)

print("======================Priority Queue===================================")
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1
messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())

