import T_Array as TArray

class VectorArray(TArray.T_Array):

    def __init__(self, vector):
        self.s = 0
        self.T = self.make_array(100)

    def size(self):
        return self.s

    def add(self, items):
        if self.s == len(self.T):
            self.T = self.resize(self.T, self.s*2)
        self.T[self.s] = items
        self.s += 1

    def append(self, items, index):
        s = self.size()
        if self.s == len(self.T):
            new_arr = self.make_array(s*2)
            j = 0
            for i in range(1, s+1):
                if not i == index:
                    new_arr[j] = self.get(i)
                else:
                    new_arr[j] = items
                    j += 1
                    new_arr[j] = self.get(i)
                j += 1
            self.T = new_arr
        else:
            for i in range(s,index-1,-1):
                self.T[i] = self.T[i - 1]
            self.T[index - 1] = items
        self.s += 1

    def get(self, index):
        return self.T[index - 1]

    def remove(self, index):
        s = self.size()
        if s > 1:
            new_arr = self.make_array(s - 1)
            j = 0
            for i in range(1, s + 1):
                if not i == index:
                    new_arr[j] = self.get(i)
                    j += 1
        elif s == 1:
            new_arr = self.make_array(self.s)
        self.s -= 1
        self.T = new_arr

    def remove_v(self, index):
        s = self.size()
        for i in range(index, s-1):
            self.T[i-1] = self.T[i]
        self.T[s-1] = None
        self.s -= 1
        if len(self.T) - self.s > self.s:
            self.resize(self.T, self.s)


    def str(self):
        self.print(self.T, self.size())

if __name__ == '__main__':
    T = VectorArray(5)
    T.add(1)
    T.add(25)
    T.add(44)
    T.add(54)
    T.add(77)
    print(T.size())
    T.str()
    T.remove(3)
    T.remove_v(1)
    T.str()
    T.append(1001, 2)
    T.str()