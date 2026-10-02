# Queue as a List

queue = []

# Enqueue elements into the queue
queue.append(1)  # Enqueue 1 into the queue
queue.append(2)  # Enqueue 2 into the queue
queue.append(3)  # Enqueue 3 into the queue
queue.append(4)  # Enqueue 4 into the queue
queue.append(5)  # Enqueue 5 into the queue

print("Queue after enqueuing elements:", queue)  # [1, 2, 3, 4, 5]

# Accessing the front element of the queue
print("Front element of the queue:", queue[0])  # 1

# Dequeue elements from the queue
print(queue.pop(0))  # Dequeue the front element (1)
print(queue.pop(0))  # Dequeue the front element (2)
print(queue.pop(0))  # Dequeue the front element (3)
print(queue.pop(0))  # Dequeue the front element (4)
print(queue.pop(0))  # Dequeue the front element (5)    