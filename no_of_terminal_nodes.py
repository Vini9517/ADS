# 4.Write method to count number of terminal nodes.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def count_terminal_nodes(self):
        return self._count_terminal_nodes(self.root)

    def _count_terminal_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        left_count = self._count_terminal_nodes(node.left)
        right_count = self._count_terminal_nodes(node.right)
        return left_count + right_count

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

terminal_nodes = bst.count_terminal_nodes()
print("Number of Terminal Nodes in the Binary Search Tree:", terminal_nodes)
