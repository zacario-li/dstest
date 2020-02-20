import random

class HashTable(object):
    def __init__(self, data):
        self.elem = [None for i in range(len(data))]
        self.count = len(data)
        for i in data:
            self.insertHash(i)
        
    def hash(self, key):
        return key % self.count
    
    def insertHash(self, key):
        addr = self.hash(key)
        while self.elem[addr] != None:
            addr = (addr+1) % self.count
        self.elem[addr] = key

    def hashSearch(self, key):
        beginning = addr = self.hash(key)
        while self.elem[addr] != key:
            addr = (addr + 1)%self.count
            if addr == beginning:
                return -1
        return addr


if __name__ == '__main__':
    data = [43,90,12,0,45,1234,984,23,5678,11]
    htbl = HashTable(data)
    ret = htbl.hashSearch(1234)
    print(f'ret index is: {ret}')