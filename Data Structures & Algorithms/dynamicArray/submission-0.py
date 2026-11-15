class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.end = 0
        self.l = []

    def get(self, i: int) -> int:
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        self.l[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.end:
            self.resize()
        self.l.append(n)
        self.end += 1

    def popback(self) -> int:
        last = self.l[-1]
        self.l = self.l[:-1]
        self.end -= 1
        return last

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.end
    
    def getCapacity(self) -> int:
        return self.capacity
