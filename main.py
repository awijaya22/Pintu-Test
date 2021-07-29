# coding=utf-8
from InMemoryCache import InMemoryCache
from EvictionManager.NoneEvictionManager import NoneEvictionManager
from EvictionManager.LRUEvictionManager import LRUEvictionManager
from EvictionManager.LFUEvictionManager import LFUEvictionManager


def runProblem1(memoryCache):
    print memoryCache.Add('key1', 'value1')
    print memoryCache.Add('key2', 'value2')
    print memoryCache.Add('key3', 'value3')
    print memoryCache.Add('key2', 'value2.1')
    print memoryCache.Get('key3')
    print memoryCache.Get('key1')
    print memoryCache.Get('key2')
    print memoryCache.Get('key3')
    print memoryCache.Get('key1')
    print memoryCache.Keys()
    try:
        memoryCache.Add('key4', 'value4')
    except Exception as e:
        print e
    print memoryCache.Keys()
    print memoryCache.Clear()
    print memoryCache.Keys()


if __name__ == '__main__':
    none = NoneEvictionManager()
    lru = LRUEvictionManager()
    lfu = LFUEvictionManager()
    cache = InMemoryCache(3, lfu)
    runProblem1(cache)
