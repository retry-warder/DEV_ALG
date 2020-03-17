import numpy as np


class Node:
    def __init__(self, key):
        self.key = key
        self.size = 1
        self.left = None
        self.right = None


def search(node: Node, key):
    if node is None:
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


def get_size(node: Node):
    if node is None:
        return 0
    else:
        return node.size


def fix_size(node: Node):
    node.size = get_size(node.left) + get_size(node.right) + 1


def insert_old(node: Node, key):
    if node is None:
        return Node(key)
    elif node.key > key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    fix_size(node)
    return node


def rotate_right(node: Node):
    q = node.left
    if q is None:
        return node
    node.left = q.right
    q.right = node
    q.size = node.size
    fix_size(node)
    return q


def rotate_left(node: Node):
    p = node.right
    if p is None:
        return node
    node.right = p.left
    p.left = node
    p.size = node.size
    fix_size(node)
    return p


def insert_root(node: Node, key):
    if node is None:
        return Node(key)
    elif key < node.key:
        node.left = insert_root(node.left, key)
        return rotate_right(node)
    else:
        node.right = insert_root(node.right, key)
    return rotate_left(node)


def insert(node: Node, key):
    if node is None:
        return Node(key)
    elif np.random.random() % node.size + 1 == 0:
        insert_root(node, key)
    elif node.key > key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    fix_size(node)
    return node


def merge(left: Node, right: Node):
    if left is None:
        return right
    elif right is None:
        return left
    elif np.random.random() % (left.size + right.size) < left.size:
        left.right = merge(left.right, right)
        fix_size(left)
        return left
    else:
        right.left = merge(left, right.left)
        fix_size(right)
        return right


def remove(node: Node, key):
    if node is None:
        return None
    elif node.key == key:
        q = merge(node.left, node.right)
        return q
    else:
        if key < node.key:
            node.left = remove(node.left, key)
        else:
            node.right = remove(node.right, key)
    return node
