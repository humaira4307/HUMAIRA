Queue = []
Queue.append('x')
Queue.append('y')
Queue.append('z')
print("Initial queue")
print(Queue)
print("\nElements dequeued from queue")
print(Queue.pop(0))
print(Queue.pop(0))
print(Queue.pop(0))
print("\nQueue after removing elements")
print(Queue)



#----------------------


from collections import deque
q = deque()
q.append('p')
q.append('q')
q.append('r')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)


#--------------------------


from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())



#---------------------------



