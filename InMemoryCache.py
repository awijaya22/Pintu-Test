class InMemoryCache:
    def __init__(self, limit, evictionManager):
        self.limit = limit
        self.evictionManager = evictionManager
        self.cache = {}

    def Add(self, key, value):
        # return int 0 if is new key, 1 if key exists
        if key in self.cache:   # key exists
            self.cache[key] = value
            self.evictionManager.Update(key)
            return 1

        # check limit
        if len(self.cache) >= self.limit:
            popKey = self.evictionManager.Pop()
            self.cache.pop(popKey)

        self.evictionManager.Push(key)
        self.cache[key] = value
        return 0

    def Get(self, key):
        # return string value of the key
        if key not in self.cache:
            return None
        self.evictionManager.Update(key)
        return self.cache[key]

    def Clear(self):
        # clear all key, return int, number of key deleted
        result = len(self.cache)
        self.cache = {}     # or del self.cache
        self.evictionManager.Clear()
        return result

    def Keys(self):
        # return array of string, all keys in cache
        return self.cache.keys()
