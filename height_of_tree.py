# 3.Write method to find the height of BST.

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

    def find_height(self):
        return self._find_height(self.root)

    def _find_height(self, node):
        if node is None:
            return -1  # Height of an empty tree is -1
        left_height = self._find_height(node.left)
        right_height = self._find_height(node.right)
        return max(left_height, right_height) + 1

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

height = bst.find_height()
print("Height of the Binary Search Tree:", height)
