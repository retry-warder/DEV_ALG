class Walk_King:
    def __init__(self, x):
        self.x = x

    def run(self):
        k = 1 << self.x
        nA = 0xFEFEFEFEFEFEFEFE
        nH = 0x7F7F7F7F7F7F7F7F
        print("k = ", k)
        p7 = ((k & nA) << 7)
        print("p7 = ", p7)
        p8 = (k << 8)
        print("p8 = ", p8)
        p9 = ((k & nH) << 9)
        print("p9 = ", p9)
        p4 = ((k & nA) >> 1)
        print("p4 = ", p4)
        p6 = ((k & nH) << 1)
        print("p6 = ", p6)
        p1 = ((k & nA) >> 9)
        print("p1 = ", p1)
        p2 = (k >> 8)
        print("p2 = ", p2)
        p3 = ((k & nH) >> 7)
        print("p3 = ", p3)
        mask = p7 | p8 | p9 | p4 | p6 | p1 | p2 | p3
        print("mask = ", mask)
        q = 0
        while mask > 0:
        #    if (1 == (mask & 1)):
        #        q+=1
        #    mask = mask >> 1
            q += 1
            mask = (mask-1) & mask
        print("q = ", q)



if __name__ == '__main__':
    K = Walk_King(27)
    K.run()
