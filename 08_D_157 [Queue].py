print("No. 4")

print("Class Queue")
class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[-1]
    def getRearMost(self):
        return self.qlist[0]

q = Queue()
q.enqueue(12)
q.enqueue(34)
q.enqueue(28)
q.enqueue(31)

print(q.qlist)
print(q.getFrontMost())
print(q.getRearMost())

print("\nClass PriorityQueue")
import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist= []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self, data, prior):
        heapq.heappush(self.qlist, (prior, data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    def getFrontMost(self):
        return self.qlist[-1]
    def getRearMost(self):
        return self.qlist[0]
    
pq = PriorityQueue()

pq.enqueue('aaa', 4)
pq.enqueue('bbb', 3)
pq.enqueue('ccc', 2)
pq.enqueue('ddd', 8)

print(pq.qlist)

print("\nNo. 5")
pq = PriorityQueue()

pq.enqueue('aaa', 4)
pq.enqueue('bbb', 3)
pq.enqueue('ccc', 2)
pq.enqueue('ddd', 8)

print(pq.qlist)
pq.dequeue()
print(pq.qlist)
pq.dequeue()
print(pq.qlist)
