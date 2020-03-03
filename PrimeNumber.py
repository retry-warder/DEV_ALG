from measure_time import timer


class PrimeNumber:
    def prime_1(self, n):
        d = 0
        for j in range(1, n + 1):
            if n % j == 0:
                d += 1
        return d == 2

    # O(n log log n)
    def prime_2_1(self, n):
        prime = [True] * (n+1)
        prime[0] = False
        prime[1] = False
        for j in range(2, n + 1):
            if prime[j]:
                for k in range(2*j, n + 1, j):  # Убираем числа, которые делятся на i
                    prime[k] = False
        primes = []  # Формируем список простых
        for i in range(2, n + 1):
            if prime[i]:
                primes.append(i)
        return primes

    # Несколько оптимизаций перебора делителей, с использованием массива.
    def prime_2_2(self, n):
        prime = [True] * (n+1)
        prime[0] = False
        prime[1] = False
        for j in range(2, n + 1):
            if prime[j]:
                for k in range(j**2, n + 1, j):  # Убираем числа, которые делятся на i
                    prime[k] = False
            if j**2>n: break
        primes = []  # Формируем список простых
        for i in range(2, n + 1):
            if prime[i]:
                primes.append(i)
        return primes

    # Решето Эратосфена со сложностью O(n)
    def prime_2_3(self, n):
        lp = [0]*(n+1)
        primes = []
        for i in range(2, n+1):
            if lp[i] == 0:
                lp[i] = i
                primes.append(i)
            for p in range(0, len(primes)):
                if (primes[p] <= lp[i]) and (primes[p] * i <= n):
                    lp[primes[p] * i] = primes[p]
        return primes

