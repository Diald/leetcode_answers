''' 641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/description/
Design your implementation of the circular double-ended queue (deque).''''

from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.len = k
        self.queue = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.len:
            self.queue.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.len:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if(len(self.queue)==0):
            return False
        self.queue.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if(len(self.queue)==0):
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        if(len(self.queue)==0):
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if(len(self.queue)==0):
            return True
        else:
            return False

    def isFull(self) -> bool:
        if(len(self.queue) == self.len):
            return True
        else:
            return False
