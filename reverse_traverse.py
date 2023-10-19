# 6.Write method to traverse the BST in descending order.

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

    def reverse_traversal(self):
        self._reverse_traversal(self.root)

    def _reverse_traversal(self, node):
        if node is not None:
            self._reverse_traversal(node.right)
            print(node.key, end=' ')
            self._reverse_traversal(node.left)


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("BST in Descending Order:")
bst.reverse_traversal()
