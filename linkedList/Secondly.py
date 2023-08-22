class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def traverse(self, node):
        while node:
            print(node.data, end=" -> ")
            node = node.next
            
doubly_linked_list = DoublyLinkedList()

doubly_linked_list.head = Node("Aldrin")
node_b = Node("Mico")
node_c = Node("Andrew")
node_d = Node("Nicko")
node_e = Node("Iber")

doubly_linked_list.head.prev = None
doubly_linked_list.head.next = node_b

node_b.prev = doubly_linked_list.head
node_b.next = node_c

node_c.prev = node_b
node_c.next = node_d

node_d.prev = node_b
node_d.next = node_e

node_e.prev = node_d
node_e.next = None

# Print value of each node
print("value of head is :", doubly_linked_list.head.data)
print("value of next to head is :", doubly_linked_list.head.next.data)

print("---")

print("value of node_b is :", node_b.data)
print("value of previous of node_b is :", node_b.prev.data)
print("value of next of node_b is :", node_b.next.data)

print("---")

print("value of node_c is :", node_c.data)
print("value of previous of node_c is :", node_c.prev.data)

print("---")

print("value of node_d is :", node_d.data)
print("value of previous of node_d is :", node_d.prev.data)

print("---")

print("value of node_e is :", node_e.data)
print("value of previous of node_e is :", node_e.prev.data)

doubly_linked_list.traverse(doubly_linked_list.head)
