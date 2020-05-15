import time
from classes import BinarySearchTree

start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# import sys
# sys.setrecursionlimit(40000)

# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node
#     def get_value(self):
#         return self.value
#     def get_next(self):
#         return self.next_node
#     def set_next(self, new_next):
#         self.next_node = new_next
# class LinkedList(Node):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def add_to_head(self, value):
#         new_node = Node(value)
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node 
#         else:
#             new_node.set_next(self.head)
#             self.head = new_node
#     def add_to_end(self, value):
#         new_node = Node(value) 
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node
#     def remove_from_head(self):
#         if not self.head:
#             return None
#         else:
#             value = self.head.get_value()
#             self.head = self.head.get_next()
#             return value
#     def print_ll_elements(self):
#         current = self.head
#         while current is not None:
#             print(current.value)
#             current = current.get_next()
#     def ll_get_next(self):
#         return self.get_next()

#     def get_same_names(self, names_2_head):
#         #get initial value from both names
#         #if they are the same, add them to the list
#         #if they are different, move onto the next value
#         #recursion this
#         global duplicates

#         current_1 = self.head
#         current_2 = names_2_head
#         print('first read:', current_1.value)
#         print('self:', self.head)

#         if current_1.value is current_2.value:
#             duplicates.append(current_1.value)
#             print('In same value', current_1.value)
#             duplicates.append(current_2.value)
        
#         current_1 = current_1.get_next()
#         current_2 = current_2.get_next()
#         print('Next Value:', current_1.value)

#         if current_1.value and current_2.value is None:
#             print('In none statement', current_1.value)
#             print('In none statement', current_2.value)
#             return print('Finished looking at everything')
#         return current_1.get_same_names(current_2)
        
#make the linked lists for each file

# ll_1 = LinkedList()
# for i in names_1:
#     ll_1.add_to_head(i)

# ll_2 = LinkedList()
# for i in names_2:
#     ll_2.add_to_head(i)

#insert head of each list into function

duplicates = []

bst_1 = BinarySearchTree(names_1)


bst_2 = BinarySearchTree(names_2)

bst_1.for_each(bst_1.get_same_names(bst_2))

# print('first head:', ll_1.head.value)
# print('what is next:', ll_1.head.get_next().value)

# names_1_head = ll_1.head
# names_2_head = ll_2.head

# ll_1.get_same_names(names_2_head)
# print(duplicates)

# duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
