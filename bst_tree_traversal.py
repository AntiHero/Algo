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

arr_in_order = []
arr_pre_order = []
arr_post_order = []


# O(n) time | O(n) space
def in_order_traverse(tree, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)

    return array


def pre_order_traverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        pre_order_traverse(tree.left, array)
        pre_order_traverse(tree.right, array)

    return array


def post_order_traverse(tree, array):
    if tree is not None:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)

    return array


print("BST traverse in order", in_order_traverse(root, arr_in_order))
print("BST traverse pre order", pre_order_traverse(root, arr_pre_order))
print("BST traverse post order", post_order_traverse(root, arr_post_order))
