import T_Array as TArray

class MatrixArray(TArray.T_Array):

    def __init__(self):
        self.s = 0
        self.vector = 5
        self.T = []

    def size(self):
        return self.s

    def add(self, items):
        if self.s % self.vector == 0:
            arr = [None]*self.vector
            self.T.append(arr)
        self.T[self.s // self.vector][self.s % self.vector] = items
        self.s += 1

    def append(self, items, index):
        s = self.size()
        if index >= s:
            self.add(items)
        elif s > 0:
            if self.s % self.vector == 0:
                arr = [None] * self.vector
                self.T.append(arr)
            for i in range((self.s-1) // self.vector, index // self.vector - 1, -1):
                if i == index // self.vector:
                    g = index % self.vector
                else:
                    g = 0
                for j in range(self.vector-1, g, -1):
                    self.T[i][j] = self.T[i][j - 1]
                self.T[i][g] = self.T[i - 1][self.vector - 1]
            self.T[index // self.vector][index % self.vector] = items
            self.s += 1

    def get(self, index):
        return self.T[index // self.vector][index % self.vector]

    def str(self):
        print("######################################################################")
        k = (self.s-1) // self.vector
        for i in range(0, k+1):
            print(self.T[i])

    def remove(self, index):
        for i in range(index // self.vector, (self.s-1) // self.vector):
            if i == index // self.vector:
                g = index % self.vector
            else:
                g = 0
            for j in range(g, self.vector-1):
                self.T[i][j] = self.T[i][j+1]
            if not (self.s % self.vector == 0 and i < (self.s // self.vector)-1):
                self.T[i][self.vector-1] = self.T[i+1][0]
            self.T[(self.s-1) // self.vector][(self.s-1) % self.vector] = None
        self.s -= 1

        k = (self.s-1) // self.vector
        if (self.s-1) % self.vector:
            k += 1
        if (k)  < len(self.T):
            self.T.pop((self.s // self.vector))

