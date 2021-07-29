class NoneEvictionManager:
    def __init__(self):
        self.keyList = []

    def Push(self, key):
        # return 0 if new keys, 1 if exists
        if key in self.keyList:
            return 1
        self.keyList.append(key)
        return 0

    def Pop(self):
        # return a key(string) that must be removed from the cache
        raise Exception("key_limit_exceeded")

    def Clear(self):
        result = len(self.keyList)
        self.keyList = []
        return result

    def Update(self, key):
        pass
