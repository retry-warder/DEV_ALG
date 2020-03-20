import math


class IntervalTree:
    def __init__(self, l):
        self.arr = [0] * l
        nMax = int(math.log2(len(self.arr) - 1) + 1)
        n = (1 << nMax)
        self.tree = [0] * 2 * (1 << nMax)
        for i in range(len(self.arr),n):
            self.arr.append(0)

    def load_from_list(self, arr=None):
        if arr is None:
            arr = []
        self.arr = arr
        nMax = int(math.log2(len(self.arr) - 1) + 1)
        self.tree = [0] * 2 * (1 << nMax)
        self.build()

    def build(self):
        nMax = int(math.log2(len(self.arr) - 1) + 1)
        n = (1 << nMax)
        self.tree = [0] * 2 * n

        for i in range(len(self.arr),n):
            self.arr.append(0)

        for i in range(n, 2 * n):
            self.tree[i] = self.arr[i - n]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def sum(self, l, r):
        #l += - 1
        #r += - 1
        ans = 0
        n = int(len(self.tree) / 2)
        l += n - 1
        r += n - 1
        while l <= r:
            if l & 1:
                ans = ans + self.tree[l]
            if not r & 1:
                ans = ans + self.tree[r]
            l = int((l + 1) / 2)
            r = int((r - 1) / 2)
        return ans

    def update(self, i, x):
        self.arr[i-1] = x
        n = int(len(self.tree) / 2)
        i = i + (n - 1)
        self.tree[i] = x
        while i > 1:
            i = i // 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]


if __name__ == '__main__':
    IT = IntervalTree(5)
    IT.update(2, 2)
    IT.update(3, 1)
    IT.update(4, 2)
    print(IT.arr)
    print(IT.tree)
    print("###########################################")
    print(IT.sum(1, 1))
    print(IT.sum(2, 2))
    print(IT.sum(3, 3))
    print(IT.sum(4, 4))
    print(IT.sum(5, 5))
    print(IT.sum(1, 5))
