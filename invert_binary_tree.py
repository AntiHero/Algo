from asyncio.windows_events import NULL
from utils import bst

root = bst.BSTNode(10)
root.insert(5)
root.insert(15)
root.insert(5)
root.insert(8)
root.insert(6)
root.insert(2)
root.insert(1)
root.insert(22)
root.display()


# O(n) time | O(d) time, wher d - depth | O(lon(n))
def invert_binary_tree_recursively(tree):
    if tree is None:
        return
    tree.right, tree.left = tree.left, tree.right
    invert_binary_tree_recursively(tree.left)
    invert_binary_tree_recursively(tree.right)


invert_binary_tree_recursively(root)
print('\n')
root.display()


# O(n) time | O(n) space
def invert_binary_tree(tree):
    queue = [tree]

    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)


invert_binary_tree(root)
print('\n')
root.display()
