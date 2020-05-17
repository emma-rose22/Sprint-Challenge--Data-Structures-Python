class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if prev is not None:
        #     temp = prev
        #     prev = node.get_next()
        #     node = temp
        #     self.reverse_list(node, prev)
        while node:
            x = node
            next_one = node.get_next()

            node.next_node = prev
            prev = x
            node = next_one

        self.head = prev

            #update the pointer
            #traverse the list

#node needs to point at next
#


#    def reverse_list(self, node, prev):
#         #set node as previous
#         if prev is not None:
#             temp = prev
#             prev = node.get_next()
#             node = temp
#             self.reverse_list(node, prev)
#         else:
#             #if self.head.get_next():
#             x = self.head.get_next()
#             prev = node
#             node = x
#             #return self.reverse_list(node, prev)

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.add_to_head(4)
ll.add_to_head(5)
ll.reverse_list(ll.head, None)
print(ll.head.value)