#2.Implement following tree traversals
# a.Inorder
# b.Preorder
# c.Postorder
# d.Levelorder

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.key, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=' ')

def levelorder_traversal(node):
    if not node:
        return
    
    queue = [node]
    while queue:
        current = queue.pop(0)
        print(current.key, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Inorder Traversal:")
inorder_traversal(root)
print()

print("Preorder Traversal:")
preorder_traversal(root)
print()

print("Postorder Traversal:")
postorder_traversal(root)
print()

print("Levelorder Traversal:")
levelorder_traversal(root)
