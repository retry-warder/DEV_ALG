class Sort:
    def __init__(self, size):
        print("#########################################################################")
        print("SIZE ARRAY: {0}".format(size))
        print("#########################################################################")
        self.base_arr = [np.random.randint(0, size) for i in range(size)]
        self.sort_base_arr = [i for i in range(size)]
        for i in range(size-size//20, size):
            self.sort_base_arr[i] = np.random.randint(0, size)
        self.shell_arr = self.base_arr.copy()
        print("Shell Sort RandArr")
        self.shellSort()
        self.heap_arr = self.base_arr.copy()
        print("Heap Sort RandArr")
        self.heap_sort()
        self.shell_arr = self.sort_base_arr.copy()
        print("Shell Sort SortArr")
        self.shellSort()
        self.heap_arr = self.sort_base_arr.copy()
        print("Heap Sort SortArr")
        self.heap_sort()

    @timer
    def shellSort(self):
        gap = len(self.shell_arr) // 2
        while gap > 0:
            for i in range(gap, len(self.shell_arr)):
                temp = self.shell_arr[i]
                j = i
                while j >= gap and self.shell_arr[j - gap] > temp:
                    self.shell_arr[j] = self.shell_arr[j - gap]
                    j = j - gap
                self.shell_arr[j] = temp
            gap = gap // 2

    def heapify(self, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and self.heap_arr[left_child] > self.heap_arr[largest]:
            largest = left_child

        if right_child < heap_size and self.heap_arr[right_child] > self.heap_arr[largest]:
            largest = right_child

        if not largest == root_index:
            self.heap_arr[root_index], self.heap_arr[largest] = self.heap_arr[largest], self.heap_arr[root_index]
            self.heapify(heap_size, largest)

    @timer
    def heap_sort(self):
        n = len(self.heap_arr)
        for i in range(n, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.heap_arr[i], self.heap_arr[0] = self.heap_arr[0], self.heap_arr[i]
            self.heapify(i, 0)
