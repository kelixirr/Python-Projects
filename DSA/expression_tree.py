from linked_binary_tree import LinkedBinaryTree
class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""
    def __init__(self, token, left=None, right=None):
        # LinkedBinaryTree initialization
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string")

        self._add_root(token)
        if left is not None:
            if token not in "+-*x/":
                raise ValueError("Token must be a valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []
        # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            # opening parenthesis
            result.append('(')
            # left subtree
            self._parenthesize_recur(self.left_child(p), result)
            result.append(p.element())  # operator
            # right subtree
            self._parenthesize_recur(self.right_child(p), result)
            # closing parenthesis
            result.append(')')
