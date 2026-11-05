class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_head(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(f"['{current.data}']")
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty"

def run_linked_list(last_name):
    print("=== 2. SINGLY LINKED LIST ===")
    sll = SinglyLinkedList()

    print("\n-- Insertion Phase --")
    for char in last_name:
        sll.append(char)
        print(f"Appended node '{char}' -> Sequence: {sll.display()}")

    print("\n-- Removal Phase --")
    while sll.head is not None:
        removed = sll.remove_head()
        print(f"Removed Head node '{removed}' -> Sequence: {sll.display()}")

    print("Linked list is now empty.\n")

if __name__ == "__main__":
    name = input("Enter Last Name: ").strip().upper()
    run_linked_list(name)