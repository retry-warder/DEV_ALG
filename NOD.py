from measure_time import timer

class NOD:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @timer
    def gcd_01(self):
        print("Вычитание")
        while not self.a == self.b:
            if self.a > self.b:
                self.a = self.a - self.b
            else:
                self.b = self.b - self.a
        self.g = self.a
        print(self.g)

    #Через остаток
    @timer
    def gcd_02(self):
        print("Остаток циклы")
        while not self.a == 0 and not self.b == 0:
            if self.a > self.b:
                self.a = self.a % self.b
            else:
                self.b = self.b % self.a
        self.g = self.a + self.b
        print(self.g)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    @timer
    def gcd_03(self):
        print("Остаток рекурсия")
        self.g = self.gcd(self.a, self.b)
        print(self.g)

    @timer
    def gcd04(self):
        if (self.a == 0):
            return self.b
        if (self.b == 0):
            return self.a
        a = self.a
        b = self.b
        s = 0
        while (a | b) & 1:
            s += 1
            a >>= 1
            b >>= 1
        while (a & 1) == 0:
            a >>= 1
        while True:
            while (b & 1) == 0:
                b >>= 1
                if a > b:
                    t = b
                    b = a
                    a = t
                b -= a
            if b != 0: break
        return a << s

    def is_odd(self,number):
        return (number & 1) == 1

    def gcd05(self, a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a == b:
            return a
        elif a == 1 or b == 1:
            return 1
        elif self.is_odd(a):
            if self.is_odd(b):
                return self.gcd05(b, abs(a - b))
            else:
                return self.gcd05(a, b >> 1)
        else:
            if self.is_odd(b):
                return self.gcd05(a >> 1, b)
            else:
                return self.gcd05(a >> 1, b >> 1) << 1
    #Через битовые операции
    @timer
    def gcd06(self):
        print("Битовые операции")
        u = self.a
        v = self.b
        print(self.gcd05(u, v))

