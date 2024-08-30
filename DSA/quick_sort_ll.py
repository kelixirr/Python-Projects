from linked_queue import LinkedQueue

def quick_sort(s):
    n = len(s)
    if n < 2:
        return

    p = s.first()     # bad choice may lead to o(n^2) in worst case. choose randomly or median of three
    l = LinkedQueue()
    e = LinkedQueue()
    g = LinkedQueue()

    while not s.is_empty():
        if s.first() < p:
            l.enqueue(s.dequeue())
        elif p < s.first():
            g.enqueue(s.dequeue())
        else:
            e.enqueue(s.dequeue())

    quick_sort(l)
    quick_sort(g)

    while not l.is_empty():
        s.enqueue(l.dequeue())
    while not e.is_empty():
        s.enqueue(e.dequeue())
    while not g.is_empty():
        s.enqueue(g.dequeue())
