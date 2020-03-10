from measure_time import timer
import numpy as np
import struct
import os


class Line_Sort:
    def __init__(self, size, cnt_buckets, type_sort):

        self.filename = "line_sort_" + str(size) + ".bin"
        self.filename_bs = "bs_sort_" + str(size) + ".bin"
        self.filename_cnt_num = "cnt_num_sort_" + str(size) + ".bin"
        self.filename_range = "range_sort_" + str(size) + ".bin"

        self.size = size
        self.cnt_buckets = cnt_buckets
        self.type_sort = type_sort
        self.arr = []
        if not os.path.isfile(self.filename):
            with open(self.filename, "wb") as file:
                for i in range(0, self.size):
                    n = np.random.randint(0, 65535)
                    file.write(struct.pack(">i", n))
            file.close()
        with open(self.filename, "rb") as file:
            for i in range(0, self.size):
                self.arr.append(struct.unpack('>i', file.read(4))[0])
            file.close()

        if self.type_sort == 1:
            print("bucket_sort")
            self.bucket_sort()
            with open(self.filename_bs, "wb") as file:
                file.truncate()
                for i in range(0, len(self.arr)):
                    file.write(struct.pack(">i", self.arr[i]))
                file.close()
        elif self.type_sort == 2:
            print("cnt_for_num_sort")
            self.bucket_sort()
            with open(self.filename_cnt_num, "wb") as file:
                file.truncate()
                for i in range(0, len(self.arr)):
                    file.write(struct.pack(">i", self.arr[i]))
                file.close()
        elif self.type_sort == 3:
            print("range_sort")
            self.range_sort()
            with open(self.filename_range, "wb") as file:
                file.truncate()
                for i in range(0, len(self.arr)):
                    #print(self.arr[i])
                    file.write(struct.pack(">i", self.arr[i]))
                file.close()


    def heapify(self, arr, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if not largest == root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            self.heapify(arr, heap_size, largest)

    def sort(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    @timer
    def bucket_sort(self):
        k = self.cnt_buckets
        arr_buckets = [[] for i in range(0, k)]
        m = max(self.arr)
        for x in range(0, self.size):
            b = (k-1) * self.arr[x] // m
            arr_buckets[b].append(self.arr[x])
        i = 0
        for b in range(0, k):
            self.sort(arr_buckets[b])
            for j in range(len(arr_buckets[b])):
                self.arr[i] = arr_buckets[b][j]
                i += 1

    @timer
    def counting_sort_for_numbers(self):
        m = max(self.arr)+1
        c = [0 for i in range(0, m)]
        for x in range(0, self.size):
            c[self.arr[x]] += 1
        i = 0
        for x in range(1,m):
            for j in range(0, c[x]):
                self.arr[i] = x
                i += 1

    @timer
    def range_sort(self):
        length = len(str(max(self.arr)))
        rang = 10
        for i in range(length):
            c = [[] for k in range(rang)]
            for x in self.arr:
                f = x // 10 ** i % 10
                c[f].append(x)
        self.arr = []
        for k in range(rang):
            self.arr = self.arr + c[k]
