import time
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

from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # lesson code
        # if value < self.value:
        #     #we know we need to go left
        #     #how do we know when to recurse again? or stop?
        #     if not self.left:
        #         # we can park our value here
        #         self.left = BinarySearchTree(value)
        #     else:
        #         self.left.insert(value)
        # else:
        #     # we know we need to go right
        #     if not self.right:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
        # end lesson code

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # we always start searching at the root
        # compare the target against the self(node)

        #criteria for returning False:
        # we know we need to go in a direction, but we have reached the end, there is nothing there
        
        if target == self.value:
            return True
        if target < self.value:
            #go left if it is a BTSNode
            if not self.left:
                #if we can't go left, then our value isn't here
                return False
            return self.left.contains(target)
        else: 
            #go right
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # lesson code

        #we just gotta keep going right
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # end lesson code

        current_max = self.value

        if self.right: 
            if current_max >= self.right.value:
                return current_max
            
            if current_max < self.right.value:
                current_max = self.right.value
                return self.right.get_max()
        else:
            return current_max

    def iterative_get_max(self):
        # 
        current_max = self.value
        # traverse the structure & update current max variable
        current = self

        while current:
            if current.value > current_max:
                current_max = current.value
            current = current.right

        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        # lesson code
        fn(self.value)
        #pass it to the left and right
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def itertive_for_each(self, fn):
        stack = []

        #add the root node
        stack.append(self)

        #loop for as long as the stack has elements
        while len(stack) > 0:
            current = stack.pop()
            #take it out to perform function
            #then get any children to do the same
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)
            
            #Depth First traversal

    def breadth_first_for_each(self, fn):
        #this does the same thing as the function above
        #but it is moving laterally across the tree rather than
        #going down the list with recursion and applying
        #it to the children and then going up 

        queue = deque()

        #add the root node
        queue.append(self)

        #loop for as long as the stack has elements
        while len(queue) > 0:
            current = queue.popleft()
            #take it out to perform function
            #then get any children to do the same
            if current.right:
                 queue.append(current.right)
            if current.left:
                 queue.append(current.left)

            fn(current.value)

    def in_order_print(self, node):

        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        to_print = deque()

        #add the root node
        to_print.append(self)

        #loop for as long as the stack has elements
        while len(to_print) > 0:
            current = to_print.popleft()
            #take it out to perform function
            #then get any children to do the same
            if current.right:
                 to_print.append(current.right)
            if current.left:
                 to_print.append(current.left)

            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #initialize stack
        #push root to stack

        print(node.value)

        if node.right:
            node.right.dft_print(node.right)
        if node.left:
            node.left.dft_print(node.left)

    def get_same_names(self, target):
        if target == self.value:
            duplicates.append(target)
        if target < self.value:
            #go left if it is a BTSNode
            if not self.left:
                #if we can't go left, then our value isn't here
                return False
            return self.left.contains(target)
        else: 
            #go right
            if not self.right:
                return False
            return self.right.contains(target)


duplicates = []

bst_1 = BinarySearchTree()
for i in names_1:
    bst_1.insert(i)

bst_2 = BinarySearchTree()
for i in names_2:
    bst_2.insert(i)
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
