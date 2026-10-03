class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        elif value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        pop_val = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == pop_val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
