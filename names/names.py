import time
from classes import BinarySearchTree

start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


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

for i in bst_1.value:
    if bst_2.value.contains(i) == True:
        duplicates.append(i)



# def get_same_names(bst_1, bst_2):
#     global duplicates

#     for i in bst_1.values:
#         if bst_2.contains(i):
#             duplicates.append(i)

#     if bst_1.right:
#         bst_1.right.get_same_names(bst_1.right, bst_2.right)
#     if bst_1.left:
#         bst_1.left.get_same_names(bst_1.left, bst_2.left)

#get_same_names(bst_1, bst_2)

#print(bst_2.value)


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
