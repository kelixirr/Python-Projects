class Empty(Exception):
    def __init__(self, message = "stack is empty"):
        self.message = message
        super().__init__(self.message)


class LinkedStack:
    """LIFO STACK USING SINGLY LINKED LIST"""

    class _Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty()
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty()
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
