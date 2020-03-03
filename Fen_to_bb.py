class Fen_to_bb:
    def __init__(self, s):
        self.d = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, "p": 7, "n": 8, "b": 9, "r": 10, "q": 11, "k": 12}
        self.b = [0] * 12
        self.s = s.split('/')

    def run(self):
        print(self.s)
        r = 8
        for i in range(len(self.s)):
            if not self.s[i].isdigit():
                k = (r * ((len(self.s) - i) - 1))
                for j in range(len(self.s[i])):
                    if self.s[i][j].isdigit():
                        k += int(self.s[i][j])
                    else:
                        if k == 0:
                            y = 1
                        else:
                            y = 2 << (k - 1)
                        self.b[self.d.get(self.s[i][j]) - 1] += y
                        k += 1
        return self.b


if __name__ == '__main__':
    f = Fen_to_bb("8/1k6/ppp4p/8/8/8/1K6/QQQQQQQQ")
    print(f.run())
