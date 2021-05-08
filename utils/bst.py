class BSTNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if not self.value:
            self.value = value
            return

        if self.value == value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = BSTNode(value)
            return

        if self.right:
            self.right.insert(value)
            return
        self.right = BSTNode(value)

    def delete(self, value):
        if self == None:
            return self
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            return self
        if value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)
        return self
