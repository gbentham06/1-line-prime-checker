def isprime(n):
    return all([False if n % i == 0 else True for i in range(2, n) if i*i <= n]) if n > 1 else False
