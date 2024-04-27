

# Creating a stack
def create_stack():
    Stack = []
    return Stack


# Creating an empty stack
def check_empty(Stack):
    return len(Stack) == 0


# Adding items into the stack
def push(Stack, item):
    Stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(Stack):
    if (check_empty(Stack)):
        return "stack is empty"

    return Stack.pop()


Stack = create_stack()
push(Stack, str(1))
push(Stack, str(2))
push(Stack, str(3))
push(Stack, str(4))
print("popped item: " + pop(Stack))
print("stack after popping an element: " + str(Stack))

