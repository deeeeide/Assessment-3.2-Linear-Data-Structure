class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def run_stack(last_name):
    print("=== 3. STACK (LIFO) ===")
    stack = Stack()

    print("\n-- Insertion Phase (Push) --")
    for char in last_name:
        stack.push(char)
        print(f"Pushed '{char}' onto Stack -> State: {stack.items}")

    print("\n-- Removal Phase (Pop) --")
    while not stack.is_empty():
        removed = stack.pop()
        print(f"Popped '{removed}' from Stack -> State: {stack.items}")

    print("Stack is now empty.\n")

if __name__ == "__main__":
    name = input("Enter Last Name: ").strip().upper()
    run_stack(name)