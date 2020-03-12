class Node:
    def __init__(self, data, right=None, left=None, parent=None):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent

    def __str__(self):
        return str(self.data)

    def setRight(self, node):
        self.right = node
        if node:
            node.parent = self

    def setLeft(self, node):
        self.left = node
        if node:
            node.parent = self
    def high(self):
        lh = self.left.high() if self.left else -1
        rh = self.right.high() if self.right else -1
        return rh + 1 if rh > lh else lh + 1
    
    def balance(self):
        lh = self.left.high() if self.left else 0
        rh = self.right.high() if self.right else 0
        return rh - lh


class BinaryTree:

    def __init__(self):
        self._root = None

    def _insert(self, node, data):
        if data > node.data:
            if node.right:
                self._insert(node.right, data)
            else:
                node.setRight(Node(data))
        elif data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.setLeft(Node(data))

    def search(self, node, data):
        if node:
            if node.data == data:
                return node
            elif node.data < data:
                return self.search(node.right, data)
            elif node.data > data:
                return self.search(node.left, data)
        else:
            return None

    def _searchMin(self, node):
        if node.left:
            return self._searchMin(node.left)
        else:
            return node

    def _searchMax(self, node):
        if node.right:
            return self._searchMax(node.right)
        else:
            return node

    def _remove(self, node):
        if node.left and node.right:
            min = self._searchMin(node.right)
            node.data = min.data
            min.parent.setRight(min.right)
        elif node.left:
            if node.parent:
                if node.parent.right:
                    node.parent.setRight(node.left)
                else:
                    node.parent.setLeft(node.left)
            else:
                self._root = node.left
                self._root.parent = None
        elif node.right:
            if node.parent:
                if node.parent.right:
                    node.parent.setRight(node.right)
                else:
                    node.parent.setLeft(node.right)
            else:
                self._root = node.right
                self._root.parent = None
        else:
            if node.parent:
                if node.parent.right:
                    node.parent.setRight(None)
                else:
                    node.parent.setLeft(None)
            else:
                self._root = None

    def insert(self, data):
        if self._root:
            self._insert(self._root, data)
        else:
            self._root = Node(data)

    def remove(self, data):
        node = self.search(self._root, data)
        if node:
            self._remove(node)


class AVLTree(BinaryTree):

    def insert(self, data):
        super().insert(data)
        self._root = self.__balance(self._root)

    def remove(self, data):
        super().remove(data)
        self._root = self.__balance(self._root)

    def __rightRotate(self, x):
        y = x.right
        x.setRight(y.left)
        y.setLeft(x)
        return y

    def __leftRotate(self, x):
        y = x.left
        x.setLeft(y.right)
        y.setRight(x)
        return y

    def __rightLeftRotate(self, x):
        x.setRight(self.__leftRotate(x.right))
        return self.__rightRotate(x)

    def __leftRightRotate(self, x):
        x.setLeft(self.__rightRotate(x.left))
        return self.__leftRotate(x)

    def __balance(self, node):
        if node.left:
            node.setLeft(self.__balance(node.left))
        if node.right:
            node.setRight(self.__balance(node.right))

        y = None
        if node.balance() < -1 or node.balance() > 1:
            if node.balance() < -1:
                if node.left.balance() < 0:
                    y = self.__leftRotate(node)
                else:
                    y = self.__leftRightRotate(node)

            if node.balance() > 1:
                if node.right.balance() > 0:
                    y = self.__rightRotate(node)
                else:
                    y = self.__rightLeftRotate(node)

            if node == self._root:
                y.parent = None

            node = y

        return node
