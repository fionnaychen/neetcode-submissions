# One instance of doubly linked list, used to keep track of LRU
class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # Dictionary is (key,ListNode)
        self.d = {}
        # Left most will be Most Recently Used (MRU)
        # Right most will be Least Recently Used (LRU)
        self.left = self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self,node):
        prev, next = self.left, self.left.next
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node


    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            cur = self.d[key]
            self.remove(cur)
            self.insert(cur) 
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            newNode = ListNode(key,value)
            self.d[key] = newNode
            self.insert(newNode)
        else:
            cur = self.d[key]
            cur.val = value
            self.remove(cur)
            self.insert(cur)
        if len(self.d) > self.cap:
            del self.d[self.right.prev.key]
            self.remove(self.right.prev)
        
