from collections import deque

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

    # def get_same_names(self, target):
    #     global duplicates

    #     if self.value == target.value:
    #         duplicates.append(self.value)

    #     if target.right:
    #         target.right.get_same_names(self.right, target.right)
    #     if target.left:
    #         target.left.get_same_names(self.left, target.left)
