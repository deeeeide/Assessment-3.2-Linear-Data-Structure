def run_array(last_name):
    print("=== 1. ARRAY ===")
    array = []

    print("\n-- Insertion Phase --")
    for i in range(len(last_name)):
        char = last_name[i]
        array.append(char)
        print(f"Set array[{i}] = '{char}' -> Current Array State: {array}")

    print("\n-- Removal Phase --")
    for i in range(len(array) - 1, -1, -1):
        removed_char = array.pop()
        print(f"Removed element at index {i} ('{removed_char}') -> Current Array State: {array}")

    print("Array is now empty.\n")

if __name__ == "__main__":
    name = input("Enter Last Name: ").strip().upper()
    run_array(name)