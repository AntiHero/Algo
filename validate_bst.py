from utils import bst

root = bst.BSTNode(10)

root.insert(5)
root.insert(5)
root.insert(2)
root.insert(1)
root.insert(15)
root.insert(20)
root.insert(13)
root.insert(22)
root.insert(14)

root.display()


# O(n) time | O(d) space d - depth of the tree
def validate_bst(tree):
    return validate_bst_helper(tree, float("-inf"), float("inf"))


def validate_bst_helper(tree, min_value, max_value):
    if tree is None:
        return True

    if tree.value < min_value or tree.value >= max_value:
        return False

    left_is_valid = validate_bst_helper(tree.left, min_value, tree.value)
    return left_is_valid and validate_bst_helper(tree.right, tree.value, max_value)


print("validate bst: ", validate_bst(root))
