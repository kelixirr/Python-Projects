import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capcacity = 1
        self._A = self._make_array(self._capcacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k <= self._n:
            raise IndexError('Invalid Index')

        return self._A[k]

    def append(self, obj):
        if self._n == self._capcacity:
            self._resize(2 * self._capcacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]

        self._A = B
        self._capcacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()
