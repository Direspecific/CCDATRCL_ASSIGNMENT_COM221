class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:

    def __init__(self):
        self.head = None

    def traverse(self, node):
        
        head = node
        
        while node:
            print(node.data, end=" -> ")
            node = node.next
            
            # Break to prevent infinite loop
            if node == head:
                break
            
circular_linked_list = CircularLinkedList()

circular_linked_list.head = Node("Aldrin")
node_b = Node("Mico")
node_c = Node("Andrew")
node_d = Node("Nicko")
node_e = Node("Iber")

circular_linked_list.head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = circular_linked_list.head


# Print value of each node
print("value of head is :", circular_linked_list.head.data)
print("value of next to head is :", circular_linked_list.head.next.data)

print("---")

print("value of node_b is :", node_b.data)
print("value of next of node_b is :", node_b.next.data)

print("---")

print("value of node_c is :", node_c.data)
print("value of next of node_c is :", node_c.next.data)

print("---")

print("value of node_d is :", node_d.data)
print("value of next of node_d is :", node_d.next.data)

print("---")

print("value of node_e is :", node_e.data)
print("value of next of node_e is :", node_e.next.data)

circular_linked_list.traverse(circular_linked_list.head)
