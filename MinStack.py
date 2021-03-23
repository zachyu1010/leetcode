class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minCached = True
        self.min = (2 ** 31) - 1

    def push(self, val):
        self.stack.append(val)
        if self.minCached == True:
            if val < self.min:
                self.min = val

    def pop(self):
        if self.stack[-1] == self.min:
            self.minCached = False
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        if self.minCached == True:
            return self.min
        else:
            m = min(self.stack)
            self.min = m
            self.minCached = True
            return m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(4)
    obj.push(2)
    obj.push(3)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print("%d %d" % (param_3, param_4))
