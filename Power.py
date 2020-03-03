from measure_time import timer
import logging

class POWER:
    def __init__(self, b, p):
        self.b = b
        self.p = p

    def pow_m(self, base, power):
        res = 1
        while power != 1:
            if power % 2 == 1:
                res *= base
            base *= base
            power //= 2
        if power > 0:
            res *= base
        return res

    @timer
    def pow_1(self):
        print("Через степень двойки с домножением")
        return self.pow_m(self.b, self.p)

    def pow_r(self, b, p):
        if p == 0:
            return 1
        if p % 2 == 0:
            return self.pow_r(b, p / 2) ** 2
        else:
            return b * self.pow_r(b, p - 1)

    @timer
    def pow_2(self):
        print("Рекурсия")
        return self.pow_r(self.b, self.p)

