from utils import bst

tree = bst.BSTNode(11)

tree.insert(7)
tree.insert(5)
tree.insert(9)
tree.insert(15)
tree.insert(13)
tree.insert(20)

tree.display()


# O(n) time | O(log(n)) space | Worst O(n) space
def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, current_sum, sums):
    if node is None:
        return
    new_current_sum = current_sum + node.value

    if node.left is None and node.right is None:
        sums.append(new_current_sum)
        return

    calculate_branch_sums(node.left, new_current_sum, sums)
    calculate_branch_sums(node.right, new_current_sum, sums)


print('branch_sums', branch_sums(tree))
