class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self, node):
        while node:
            print(node.data, end=" -> ")
            node = node.next

linked_list = LinkedList()

linked_list.head = Node("aldrin")
node_b = Node("mico")
node_c = Node("Andrew")
node_d = Node("Nicko")
node_e = Node("Iber")

linked_list.head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e

linked_list.traverse(linked_list.head)
