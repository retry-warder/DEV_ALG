from measure_time import timer
import math

class FIB:
    def __init__(self, n):
        self.n = n

    def fib_reccurent(self, n):
        if n < 3:
            return 1
        return self.fib_reccurent(n - 1) + self.fib_reccurent(n - 2)

    @timer
    def fib_01(self):
        print("Рекурсия")
        print(self.fib_reccurent(self.n))

    def fibIter(self, a, b, count):
        if count==0:
            return b
        else:
            return self.fibIter(a+b, a, count-1)

    @timer
    def fib_02(self):
        print("Итерации")
        print(self.fibIter(1, 0, self.n))

    @timer
    def fib_03(self):
        print("Не рекурсивный")
        fib1=fib2=1
        i = 2
        fib_sum = 0
        while i < self.n:
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum
            i += 1
        print(fib_sum)

    @timer
    def fib_04(self):
        print("Динамическое прогр.")
        a = 0
        b = 1
        for i in range(self.n):
            a, b = b, a + b
        print(a)

    @timer
    def fib_05(self):
        print("золотое сечение")
        S = math.sqrt(5)
        P = (S + 1) / 2
        print(int(P ** self.n / S + 0.5))

    #Матрицами
    def pow(self, x, n, i, mult):
        if n == 0:
            return i
        elif n == 1:
            return x
        else:
            y = self.pow(x, n//2, i, mult)
            y = mult(y, y)
            if n % 2:
                y = mult(x, y)
            return y


    def identity_matrix(self, n):
        r = list(range(n))
        return [[1 if i == j else 0 for i in r] for j in r]


    def matrix_multiply(self, A, B):
        BT = list(zip(*B))
        return [[sum(a * b for a, b in zip(row_a, col_b))
                for col_b in BT]
                for row_a in A]

    @timer
    def fib_06(self):
        print("Матричный алгоритм")
        F = self.pow([[1, 1], [1, 0]], self.n, self.identity_matrix(self.n), self.matrix_multiply)
        print(F[0][1])

