class Empty(Exception):
    def __init__(self, message = "Queue is empty"):
        super().__init__(message)
        self.message = message

class CircularQueue:

    class _Node:
        __slots__ = "_elements", "_next"
        def __init__(self, elements, next):
            self._elements = elements
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty()
        head = self._tail._next
        return head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size +=

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

    def dequeue(self):
        if self.is_empty():
            raise Empty()
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element