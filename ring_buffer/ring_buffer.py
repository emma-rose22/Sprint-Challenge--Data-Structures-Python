from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = deque()

    def append(self, item):
        self.storage.append(item)
        if len(self.storage) > self.capacity:
            self.storage.popleft()

    def get(self):
        return list(self.storage)