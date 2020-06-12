class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [0 for i in range(capacity)] #creates the array the size of capacity
        self.oldest_index = 0 #tracking the index is key to respecting capacity

    def append(self, item):
        self.storage[self.oldest_index] = item #rewrite the oldest value
        #print('first oldest index', self.oldest_index)
        self.oldest_index = (self.oldest_index + 1) % self.capacity
        #incrementing the index by one to ensure we don't overwrite wrong stuff
        #mod operand makes sure we wont ever go over the index value of capacity
        #print('second oldest index:', self.oldest_index)
    def get(self):
        #this part is just adding everything to a list to print it
        values = []
        for i in self.storage:
            if i:
                values.append(i)
        return values


ring = RingBuffer(10)
ring.append(4)
print()
ring.append(92)
print()
ring.append(23)
print()
ring.append(23)
print()
ring.append(23)
print()
ring.append(23)
print()
ring.append(23)
print()
ring.append(23)
print()
ring.append(23)
print()
ring.append(23)
print()

print(ring.get())