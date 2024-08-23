from abstract_tree import Tree

class BinaryTree(Tree):
    def left_child(self, p):
        raise NotImplementedError("Must be implemented by subclass")
    def right_child(self, p):
          raise NotImplementedError("Must be implemented by subclass")
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left_child(parent):
                return self.right_child(parent)
            else:
                return self.left_child(parent)
    def chidren(self, p):
        if self.left_child(p) is not None:
            yield self.left_child(p)
        if self.right_child(p) is not None:
            yield self.right_child(p)
