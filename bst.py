# Node Class
class Node:
    # Constructor that assigns the value, left and right nodes
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # If node is not a leaf, wrap its children and value into parentheses
    def __str__(self):
        if self.left and self.right:
            return f"({str(self.left)} {self.value} {str(self.right)})"
        else:
            return str(self.value)

    # Recursive function to evaluate the expression represented by the binary tree
    def evaluate(self):
        # If the value of the node is an operator, perform the operation on the results of the left and right child
        if self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        if self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        if self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        if self.value == '/':
            return self.left.evaluate() / self.right.evaluate()
        if self.value == '%':
            return self.left.evaluate() % self.right.evaluate()
        if self.value == '^':
            return self.left.evaluate() ** self.right.evaluate()
        # If the node is a leaf (no children), return its value as integer
        else:
            return int(self.value)


# class to represent the entire expression tree
class EvaluateTree:
    # Constructor with an optional root node
    def __init__(self, root=None):
        self.root = root
    # String representation of the tree (represented by the root)
    def __str__(self):
        return str(self.root)
    # Function to start evaluating the expression tree from the root
    def evaluate(self):
        return self.root.evaluate()
    def about(self):
        return "*** Jacob Francis // CSC 130 ***"


# Test the EvaluateTree and Node classes
if __name__ == "__main__":
    # Define test cases as pairs of expression strings and corresponding binary trees
    expressions = [
        ("(5 + (7 / 2))", Node('+', Node(5), Node('/', Node(7), Node(2)))), # result should be 8.5
        ("(2.5 * (1 + 4))", Node('*', Node(2.5), Node('+', Node(1), Node(4)))), # result should be 10
        ("((5 * 25) / (27 - 2))", Node('/', Node('*', Node(5), Node(25)), Node('-', Node(27), Node(2)),)), # result should be 5
        ("((10 ^ 2) - 1)", Node('-', Node('^', Node(10), Node(2)), Node(1))), # result should be 99
        ("(((3 + 2) * 4) / 2)", Node('/', Node('*', Node('+', Node(3), Node(2)), Node(4)), Node(2))), # result should be 10
        ("((7 % 3) + 8)", Node('+', Node('%', Node(7), Node(3)), Node(8))), # result should be 9
        ("((10 / 2) * (3 + 2))", Node('*', Node('/', Node(10), Node(2)), Node('+', Node(3), Node(2)))), # result should be 25
        ("((4 ^ 3) - (2 * 2))", Node('-', Node('^', Node(4), Node(3)), Node('*', Node(2), Node(2)))), # result should be 60
        ("(((5 + 3) % 3) * 10)", Node('*', Node('%', Node('+', Node(5), Node(3)), Node(3)), Node(10))), # result should be 20
        ("(((10 * 10) / 5) ^ 2)", Node('^', Node('/', Node('*', Node(10), Node(10)), Node(5)), Node(2))), # result should be 400
    ]
    tree=EvaluateTree()
    print(tree.about()) # Outputs: Jacob Francis // CSC 130
    # loop to Iterate through test cases
    for expression, root in expressions:
        # Initialize the tree with the root node of the test case
        tree = EvaluateTree(root)
        # Print the string representation of the expressions and prints the result
        print(f"{expression} --> {tree.evaluate()}")
