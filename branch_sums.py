from utils import bst

# binary search tree
tree = bst.BSTNode(11)

tree.insert(7)
tree.insert(5)
tree.insert(9)
tree.insert(15)
tree.insert(13)
tree.insert(20)

# O(n) time | O(log(n)) space | Worst O(n) space


def branchSums(root):
    sums = []
    caculateBranchSums(root, 0, sums)
    return sums


def caculateBranchSums(node, currentSum, sums):
    if node is None:
        return
    newCurrentSum = currentSum + node.value

    if node.left is None and node.right is None:
        sums.append(newCurrentSum)
        return

    caculateBranchSums(node.left, newCurrentSum, sums)
    caculateBranchSums(node.right, newCurrentSum, sums)


print('branchSums', branchSums(tree))
