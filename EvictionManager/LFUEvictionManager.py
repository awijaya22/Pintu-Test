import heapq

class LFUEvictionManager:
    def __init__(self):
        self.nodeMap = {}
        self.heap = []
        heapq.heapify(self.heap)

    def Push(self, key):
        node = Node(key, 1)
        self.nodeMap[key] = node
        heapq.heappush(self.heap, node)
        return 0

    def Pop(self):
        while self.heap:
            popNode = heapq.heappop(self.heap)
            if popNode.removed is False:
                self.nodeMap.pop(popNode.key)
                return popNode.key
        return None

    def Clear(self):
        self.nodeMap = {}
        self.heap = []
        heapq.heapify(self.heap)

    def Update(self, key):
        oldNode = self.nodeMap[key]
        oldNode.removed = True
        newNode = Node(key, oldNode.freq+1)
        heapq.heappush(self.heap, newNode)

class Node:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
        self.removed = False

    def __lt__(self, other):
        return self.freq < other.freq
