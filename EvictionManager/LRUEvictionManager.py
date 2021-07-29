class LRUEvictionManager:
    def __init__(self):
        self.nodeMap = {}
        self.head = Node(-1)
        self.tail = Node(-1, prevNode=self.head)
        self.head.nextNode = self.tail

    def Push(self, key):
        if key in self.nodeMap:
            return 1

        self.nodeMap[key] = self._NewNode(key)
        return 0

    def Pop(self):
        # self._PrintNode()
        popNode = self.head.nextNode
        self.head.nextNode = self.head.nextNode.nextNode
        self.head.nextNode.prevNode = self.head
        return popNode.key

    def Clear(self):
        self.nodeMap = {}
        self.head = Node(-1)
        self.tail = Node(-1, prevNode=self.head)
        self.head.nextNode = self.tail

    def Update(self, key):
        node = self.nodeMap[key]
        node.prevNode.nextNode = node.nextNode
        node.nextNode.prevNode = node.prevNode
        node.prevNode = self.tail.prevNode
        self.tail.prevNode.nextNode = node
        node.nextNode = self.tail
        self.tail.prevNode = node

    def _NewNode(self, key):
        newNode = Node(key)
        newNode.prevNode = self.tail.prevNode
        self.tail.prevNode.nextNode = newNode
        self.tail.prevNode = newNode
        newNode.nextNode = self.tail
        return newNode

    def _PrintNode(self):
        print "StartNode"
        node = self.head
        while node is not None:
            print node.key
            node = node.nextNode
        print "EndNode"

class Node:
    def __init__(self, key, prevNode=None, nextNode=None):
        self.key = key
        self.prevNode = prevNode
        self.nextNode = nextNode
