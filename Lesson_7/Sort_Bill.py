import numpy as np
import struct
import os
import operator
from measure_time import timer

class Sort_Bill:
    def __init__(self, size, r):
        self.filename = "Sort_Bill_" + str(size) + ".bin"
        self.filename_i = "Sort_Bill_" + str(size)
        self.filename_sort = "Sort_Bill_" + str(size) + "_SORT.bin"
        self.size = size
        self.r = r
        if not os.path.isfile(self.filename):
            with open(self.filename, "wb") as file:
                for i in range(size):
                    n = np.random.randint(0, 65535)
                    #print(n)
                    file.write(struct.pack(">i", n))
            file.close()
        self.file_sort()

    def merge(self, left, right, compare):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    def merge_sort(self, L, compare=operator.lt):
        if len(L) < 2:
            return L[:]
        else:
            middle = len(L) // 2
            left = self.merge_sort(L[:middle], compare)
            right = self.merge_sort(L[middle:], compare)
            return self.merge(left, right, compare)

    @timer
    def file_sort(self):
        q = self.size // self.r
        o = self.size % self.r
        b = 0
        with open(self.filename, "rb") as file:
            for j in range(1, self.r + 1):
                arr = []
                if j == self.r:
                    e = j * q + o
                else:
                    e = j * q
                for h in range(b, e):
                    arr.append(struct.unpack('>i', file.read(4))[0])
                arr = self.merge_sort(arr)
                with open(self.filename_i + "_" + str(j) + ".bin", "wb") as file_j:
                    file_j.truncate()
                    for g in range(0, len(arr)):
                        file_j.write(struct.pack(">i", arr[g]))
                    file_j.close()
                b = e
        arr_base = []
        for j in range(1, self.r + 1):
            arr = []
            if j == self.r:
                e = q + o
            else:
                e = q
            with open(self.filename_i + "_" + str(j) + ".bin", "rb") as file:
                for i in range(0, e):
                    if j == 1:
                        arr_base.append(struct.unpack('>i', file.read(4))[0])
                    else:
                        arr.append(struct.unpack('>i', file.read(4))[0])
                file.close()
            arr_base = self.merge(arr_base, arr, operator.lt)
        with open(self.filename_sort, "wb") as file:
            file.truncate()
            for i in range(0, len(arr_base)):
                file.write(struct.pack(">i", arr_base[i]))
            file.close()

if __name__ == '__main__':
    FS = Sort_Bill(1000000000, 10)
