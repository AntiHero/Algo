class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Avg: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        return self

    # Avg: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node:
                current_node = current_node.right
            else:
                return True

        return False

    def remove(self, value, parent_node=None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = BST.get_min_value(current_node.right)
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.right = current_node.right.right
                        current_node.left = current_node.right.left
                    else:
                        current_node.value = None
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    @staticmethod
    def get_min_value(current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    @staticmethod
    def get_max_value(current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    @staticmethod
    def print(node=None, level=0):
        if node is not None:
            BST.print(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            BST.print(node.left, level + 1)


tree = BST(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(5)
tree.insert(13)
tree.insert(22)

BST.print(tree)
tree.remove(10)
BST.print(tree)
