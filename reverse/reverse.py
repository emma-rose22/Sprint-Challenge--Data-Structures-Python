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
        if node is None:
            #if its empty
            return None
        if node.next_node is None:
            #if there is only one value
            self.head = node
            return node

        prev = node.next_node
        rev = self.reverse_list(prev, node)

        #next next is current
        node.next_node.next_node = node
        #next is the previous 
        node.next_node = rev
        #head is the next
        self.head = node.next_node
        return node.next_node

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.add_to_head(4)
# ll.add_to_head(5)

ll.reverse_list(ll.head, None)