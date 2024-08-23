from binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', "_parent", '_left_child', '_right_child'
        def __init__(self, element, parent = None, left_child = None, right_child = None):
            self._element = element
            self._parent = parent
            self._left_child = left_child
            self._right_child = right_child

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._element is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0
    def __len(self):
        return self._size
    def root(self):
        return self._make_position(self._root)
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def left_child(self, p):
        node = self._validate(p)
        return self._make_position(node._left_child)
    def right_child(self, p):
        node = self._validate(p)
        return self._make_position(node._right_child)

    def num_childern(self, p):
        node = self._validate(p)
        count = 0
        if node._left_child is not None:
            count += 1
        if node._right_child is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: raise ValueError("Root exist")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left_child(self, p, e):
        node = self._validate(p)
        if node._left_child is not None: raise ValueError('left child exists')
        self._size += 1
        node._left_child = self._Node(e, node)
        return self._make_position(node._left_child)

    def _add_right_child(self, p, e):
        node = self._validate(p)
        if node._right_child is not None:raise ValueError('Right child exist')
        self._size += 1
        node._right_child = self._Node(e, node)
        return self._make_position(node._right_child)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left_child if node._left_child else node._right_child
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left_child:
                parent_left_child = child
            else:
                parent._right_child = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):raise ValueError('position must be leaf')
        if not type(self) is type(1) is type(2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left_child = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right_child = t2._root
            t2._root = None
            t2._size = 0

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left_child(p) is not None:
            for other in self._subtree_inorder(self.left_child(p)):
                yield other
        yield p
        if self.right_child(p) is not None:
            for other in self._subtree_inorder(self.right_child(p)):
                yield other

    def positions(self):
        return self.inorder()
