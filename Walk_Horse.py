class Walk_Horse:
    def __init__(self, x):
        self.x = x

    def run(self):
        k = 1 << self.x

        nA  = 0xFeFeFeFeFeFeFeFe
        nAB = 0xFcFcFcFcFcFcFcFc
        nH = 0x7f7f7f7f7f7f7f7f
        nGH = 0x3f3f3f3f3f3f3f3f

        print("k = ", k)

        p1 = (k << 6)
        p2 = (k >> 10)
        p3 = (k << 15)
        p4 = (k >> 17)
        p5 = (k << 17)
        p6 = (k >> 15)
        p7 = (k << 10)
        p8 = (k >> 6)

        mask = nGH & (p1 | p2) | nH & (p3 | p4) | nA & (p5 | p6) | nAB & (p7 | p8)
        print("mask = ",mask)
        q = 0
        while mask > 0:
            q += 1
            mask = (mask-1) & mask
        print("q = ", q)

