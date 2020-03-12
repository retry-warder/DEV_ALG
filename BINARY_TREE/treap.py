import numpy as np


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prior = np.random.random()
        self.left = None
        self.right = None


def split(root, data):
    if root is None:
        return None, None
    elif root.data is None:
        return None, None
    else:
        if data < root.data:
            left, root.left = split(root.left, data)
            return left, root
        else:
            root.right, right = split(root.right, data)
            return root, right


def merge(left, right):
    if (not left) or (not right):
        return left or right
    elif left.prior < right.prior:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right


def insert(root: Node, data):
    node = Node(data)
    left, right = split(root, data)
    return merge(merge(left, node), right)


def remove(root: Node, data):
    left, right = split(root, data - 1)
    f, right = split(right, data)
    return merge(left, right)
