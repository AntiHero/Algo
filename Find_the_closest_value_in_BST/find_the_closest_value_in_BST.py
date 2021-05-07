import bst

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

# Avg O(log(n)) time | Worst O(n) time | Avg O(log(n)) space | Worst O(n) space

def findClosestValueInBst1(tree, target):
    return findClosestValueInBstHelper1(tree, target, float("inf"))


def findClosestValueInBstHelper1(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper1(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper1(tree.right, target, closest)
    else:
        return closest

print('findClosestValueInBst1', findClosestValueInBst1(tree, 12))


def findClosestValueInBst2(tree, target):
    return findClosestValueInBstHelper2(tree, target, float("inf"))


# Avg O(log(n)) time | Worst O(n) time | Avg O(1) space | Worst O(1) space
def findClosestValueInBstHelper2(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target > currentNode.value:
           currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break

    return closest

print('findClosestValueInBst2', findClosestValueInBst2(tree, 12))