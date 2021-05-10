from utils import bst

tree = bst.BSTNode(15)

tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(16)
tree.insert(22)

tree.display()


# O(n) time | O(h) space
def count_node_depth(btree):
    depth_sum = 0
    stack = [{"node": btree, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        depth_sum += depth
        stack.append({"node": node.right, "depth": depth + 1})
        stack.append({"node": node.left, "depth": depth + 1})

    return depth_sum


print('count_node_depth', count_node_depth(tree))


# O(n) time | O(h) space
def count_node_depth_recursive(btree, depth=0):
    if btree is None:
        return 0
    print(depth)
    return depth + count_node_depth_recursive(btree.right, depth + 1) + count_node_depth_recursive(btree.left, depth + 1)


print('count_node_depth_recursive', count_node_depth_recursive(tree))
