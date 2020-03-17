class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


def set_parent(child: Node, parent: Node):
    if child is not None:
        child.parent = parent


def keep_parent(v: Node):
    set_parent(v.left, v)
    set_parent(v.right, v)


def rotate(parent: Node, child: Node):
    g_parent = parent.parent
    if g_parent is not None:
        if g_parent.left == parent:
            g_parent.left = child
        else:
            g_parent.right = child

    if parent.left == child:
        parent.left, child.right = child.right, parent
    else:
        parent.right, child.left = child.left, parent

    keep_parent(child)
    keep_parent(parent)
    child.parent = g_parent


def splay(node: Node):
    if node.parent is None:
        return node
    parent = node.parent
    g_parent = parent.parent
    if g_parent is None:
        rotate(parent, node)
        return node
    else:
        zigzig = (g_parent.left == parent) == (parent.left == node)
        if zigzig:
            rotate(g_parent, parent)
            rotate(parent, node)
        else:
            rotate(parent, node)
            rotate(g_parent, node)
        return splay(node)


def search(v: Node, key):
    if v is None:
        return None
    if key == v.key:
        return splay(v)
    if key < v.key and v.left is not None:
        return search(v.left, key)
    if key > v.key and v.right is not None:
        return search(v.right, key)
    return splay(v)


def split(root: Node, key):
    if root is None:
        return None, None
    root = search(root, key)
    if root.key == key:
        set_parent(root.left, None)
        set_parent(root.right, None)
        return root.left, root.right
    if root.key < key:
        right, root.right = root.right, None
        set_parent(right, None)
        return root, right
    else:
        left, root.left = root.left, None
        set_parent(left, None)
        return left, root


def insert(root: Node, key):
    left, right = split(root, key)
    root = Node(key, left, right)
    keep_parent(root)
    return root


def merge(left: Node, right: Node):
    if right is None:
        return left
    if left is None:
        return right
    right = search(right, left.key)
    right.left, left.parent = left, right
    return right


def remove(root: Node, key):
    root = search(root, key)
    set_parent(root.left, None)
    set_parent(root.right, None)
    return merge(root.left, root.right)
