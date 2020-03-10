from abc import ABC, abstractmethod
import ctypes

class T_Array(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def append(self, item, index):
        pass

    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def get(self, index):
        pass

    def print(self, T, size):
        s = []
        for x in range(size):
            s.append(str(T[x]))
        print(s)

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def resize(self, arr, delta):
        new_arr = self.make_array(len(arr) + delta)
        if len(arr) > 0:
            for j in range(len(arr)):
                new_arr[j] =arr[j]
        return new_arr
