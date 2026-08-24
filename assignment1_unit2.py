import timeit

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_dp(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_fast_doubling(n):
    def _fib_pair(k):
        if k == 0:
            return (0, 1)

        a, b = _fib_pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b

        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return _fib_pair(n)[0]


if __name__ == "__main__":
    n = 10

    print(f"Computing Fibonacci({n}) with four different approaches:\n")
    print(f"[1] Naive recursion : {fib_recursive(n)}")
    print(f"[2] Memoized recursion : {fib_memo(n)}")
    print(f"[3] Iterative DP : {fib_dp(n)}")
    print(f"[4] Fast doubling : {fib_fast_doubling(n)}")

    print("\nFirst 15 Fibonacci numbers:")
    print([fib_dp(i) for i in range(15)])

    n_big = 28
    t_naive = timeit.timeit(lambda: fib_recursive(n_big), number=1)
    t_dp = timeit.timeit(lambda: fib_dp(n_big), number=1)

    print(f"\nTiming fib({n_big}):")
    print(f" naive recursion : {t_naive:.5f} sec")
    print(f" iterative DP : {t_dp:.8f} sec")

    n_huge = 100
    print(f"\nFibonacci({n_huge}) via iterative DP : {fib_dp(n_huge)}")
    print(f"Fibonacci({n_huge}) via fast doubling : {fib_fast_doubling(n_huge)}")
