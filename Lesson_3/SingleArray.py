import T_Array as TArray

class SingleArray(TArray.T_Array):

    def __init__(self):
        self.s = 0
        self.capacity = 1
        self.T = self.make_array(self.capacity)


    def size(self):
        return self.s

    def add(self, items):
        if self.size() == 0:
            self.T[0] = items
        else:
            self.T = self.resize(self.T, 1)
            self.T[len(self.T)-1] = items
        self.s += 1

    def append(self, items, index):
        s = self.size()
        if index >= s:
            self.add(items)
        elif s > 0:
            new_arr = self.make_array(s + 1)
            j = 0
            for i in range(0, s):
                if not i == index:
                    new_arr[j] = self.get(i)
                else:
                    new_arr[j] = items
                    j += 1
                    new_arr[j] = self.get(i)
                j += 1
            self.s += 1
            self.T = new_arr

    def get(self, index):
        return self.T[index]

    def remove(self, index):
        s = self.size()
        if s > 1:
            new_arr = self.make_array(s - 1)
            j = 0
            for i in range(0,s):
                if not i == index:
                    new_arr[j] = self.get(i)
                    j += 1
        elif s == 1:
            new_arr = self.make_array(self.capacity)
        self.s -= 1
        self.T = new_arr

    def str(self):
        self.print(self.T, self.size())


if __name__ == '__main__':
    T = SingleArray()
    T.add(1)
    T.add(25)
    T.add(44)
    T.add(54)
    T.add(77)
    print(T.size())
    T.str()
    T.remove(3)
    T.remove(1)
    T.str()
    T.append(1001, 2)
    T.str()