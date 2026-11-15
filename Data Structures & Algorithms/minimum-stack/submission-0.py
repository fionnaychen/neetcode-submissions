class MinStack:

    def __init__(self):
        self.stack = []
        self.last_ind = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.last_ind += 1

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.last_ind -= 1

    def top(self) -> int:
        return self.stack[self.last_ind]

    def getMin(self) -> int:
        return min(self.stack)
        
