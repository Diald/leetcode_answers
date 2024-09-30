''' 1381. Design a Stack With Increment Operation 
https://leetcode.com/problems/design-a-stack-with-increment-operation/description
'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if(len(self.stack)!= self.size):
            self.stack.append(x)
            return
        else:
            return -1

    def pop(self) -> int:
        if(self.stack):
            return self.stack.pop()
        else:
            return -1
    def increment(self, k: int, val: int) -> None:
        if(self.stack):
            if(len(self.stack)>=k):
                for i in range(0,k):
                    self.stack[i] += val
            else:
                for i in range(len(self.stack)):
                    self.stack[i] += val
        return None
