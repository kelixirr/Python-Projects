class Empty(Exception):
    def __init__(self, message = "stack is empty"):
        self.message = message
        super().__init__(self.message)

class ArrayStack:
    """Stack implementation using a Python list"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

if __name__ == "__main__":

    def is_matched(expr):
        lefty = '({['
        righty = ')}]'
        S = ArrayStack()
        for c in expr:
            if c in lefty:
                S.push(c)
            elif c in righty:
                if S.is_empty():
                    return False
                if righty.index(c) != lefty.index(S.pop()):
                    return False
        return S.is_empty()

    print(is_matched("( )(( )){([( )])}")) # return True
