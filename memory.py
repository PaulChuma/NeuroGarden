# Simple memory store
class Memory:
    def __init__(self):
        self.entries = []

    def remember(self, item):
        self.entries.append(item)

    def recall(self):
        return self.entries[-5:]
