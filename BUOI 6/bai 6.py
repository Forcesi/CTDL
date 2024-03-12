class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def delete_node_at_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Invalid index. Index must be within the range [0, length-1].")

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
            self.length -= 1
            return deleted_node

        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        deleted_node = prev_node.next
        prev_node.next = deleted_node.next
        deleted_node.next = None
        self.length -= 1
        return deleted_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)

deleted_node = my_linked_list.delete_node_at_index(1)
print(f"Deleted node value: {deleted_node.value}")

my_linked_list.display()