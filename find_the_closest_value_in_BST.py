from utils import bst

# binary search tree
tree = bst.BSTNode(10)

tree.insert(1)
tree.insert(5)
tree.insert(5)
tree.insert(2)
tree.insert(13)
tree.insert(19)
tree.insert(22)
tree.insert(12)

tree.display()


# Avg O(log(n)) time | Worst O(n) time | Avg O(log(n)) space | Worst O(n) space
def find_closest_value_in_bst1(btree, target):
    return find_closest_value_in_bst_helper1(btree, target, float("inf"))


def find_closest_value_in_bst_helper1(btree, target, closest):
    if btree is None:
        return closest
    if abs(target - closest) > abs(target - btree.value):
        closest = btree.value
    if target < btree.value:
        return find_closest_value_in_bst_helper1(btree.left, target, closest)
    elif target > btree.value:
        return find_closest_value_in_bst_helper1(btree.right, target, closest)
    else:
        return closest


print('find_closest_value_in_bst1', find_closest_value_in_bst1(tree, 12))


def find_closest_value_in_bst2(btree, target):
    return find_closest_value_in_bst_helper2(btree, target, float("inf"))


# Avg O(log(n)) time | Worst O(n) time | Avg O(1) space | Worst O(1) space
def find_closest_value_in_bst_helper2(btree, target, closest):
    current_node = btree

    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target > current_node.value:
            current_node = current_node.right
        elif target < current_node.value:
            current_node = current_node.left
        else:
            break

    return closest


print('find_closest_value_in_bst2', find_closest_value_in_bst2(tree, 12))
