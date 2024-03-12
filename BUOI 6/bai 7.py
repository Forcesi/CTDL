class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list:")
llist.print_list()

llist.reverse()
print("\nReversed linked list:")
llist.print_list()

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_util(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next_node = curr.next
        curr.next = prev
        self.reverse_util(next_node, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverse_util(self.head, None)

llist.reverse()
print("\nReversed linked list:")
llist.print_list()