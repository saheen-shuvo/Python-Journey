# Stack as a List

stack = []

# pusing elements onto the stack
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
stack.append(3)  # Push 3 onto the stack
stack.append(4)  # Push 4 onto the stack
stack.append(5)  # Push 5 onto the stack

print("Stack after pushing elements:", stack)  # [1, 2, 3, 4, 5]

# popping elements from the stack
print(stack.pop())  # Pop the top element (5)
print(stack.pop())  # Pop the top element (4)
print(stack.pop())  # Pop the top element (3)
print(stack.pop())  # Pop the top element (2)
print(stack.pop())  # Pop the top element (1)

# getting top element of the stack
stack.append(10)  # Push 10 onto the stack
print("Top element of the stack:", stack[-1])  # 10