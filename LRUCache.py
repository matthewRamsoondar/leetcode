class Node:
    def __init__(self, key: int, val: int):
        self.val = val;
        self.key = key
        self.prev: Node = None
        self.next: Node =  None

    def __repr__(self):
        return str(self.key)
    
    def __str__(self):
        return str(self.key)

class LRUCache:
    def __init__(self, capacity: int):
        self.table: dict[int, Node] = {}
        self.head: Node = None
        self.n = capacity
        self.k = 0
        

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        if self.k <= 1:
            return self.table[key]

        cur = self.table[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        cur.prev = self.head.prev # set the previous pointer of cur
        cur.next = self.head # set the next pointer of cur
        self.head.prev.next = cur # set the tail to point to cur
        self.head.prev = cur  # set the prev pointer of head
        self.head = cur # update head

        return cur.val


    def put(self, key: int, value: int) -> None:
        if key in self.table:
            cur = self.table[key]
            cur.val = value
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.next = self.head
            cur.prev = self.head.prev
            self.head.prev = cur
            self.head.prev.next = cur
            self.head = cur
            return
            
        if self.k < self.n: # inserting a new node
            self.table[key] = Node(key, value)
            cur = self.table[key]
            self.k += 1

            if self.head is None:
                self.head = cur
                return

            if self.head.prev is None: # inserting the second node
                self.head.prev = cur 
                self.head.next = cur
                cur.next = self.head
                cur.prev = self.head
                self.head = cur
                return
            
            self.head.prev.next = cur # update tail to point to new head
            cur.prev = self.head.prev # update new head to point to tail
            cur.next = self.head # update new head to point to old head
            self.head.prev = cur # update old head to point to new head
            self.head = cur # swap head pointer
        elif self.k == 1:
            self.head.key = key
            self.head.val = value
        else: # evicting to insert a new node
            evictKey = self.head.prev.key
            self.head.prev.key = key
            self.head.prev.val = value
            self.table[key] = self.table[evictKey]
            del self.table[evictKey]

            self.head = self.head.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

a = LRUCache(3)
# a.put(2, 2)
# a.put(1, 1)
# a.put(1, 3)
a.put(2, 1)
a.get(2)

cur = a.head
res = str(a.head)
while (cur.next != None and cur.key != a.head.key):
    res += f" <-> {cur}"
    cur = cur.next
print(res)