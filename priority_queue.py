class PriorityQueue():
    def __init__(self) -> None:
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest= 0
            for i in range(1,self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]
#heap이랑 비슷함 가장 큰원소부터 뺄수있음!
q=PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("pQueue",q.items)
while not q.isEmpty():
    print("Mx Priority = ",q.dequeue())
