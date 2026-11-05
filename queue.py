from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

def run_queue(last_name):
    print("=== 4. QUEUE (FIFO) ===")
    queue = Queue()

    print("\n-- Insertion Phase (Enqueue) --")
    for char in last_name:
        queue.enqueue(char)
        print(f"Enqueued '{char}' into Queue -> State: {list(queue.items)}")

    print("\n-- Removal Phase (Dequeue) --")
    while not queue.is_empty():
        removed = queue.dequeue()
        print(f"Dequeued '{removed}' from Queue -> State: {list(queue.items)}")

    print("Queue is now empty.\n")

if __name__ == "__main__":
    name = input("Enter Last Name: ").strip().upper()
    run_queue(name)