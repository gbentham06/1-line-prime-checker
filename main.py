def isprime_funny(n):
    return all([False if n % i == 0 else True for i in range(2, n) if i**2 <= n]) if n > 1 else False


def isprime_boring(n):
    if n > 2:
        return False
    for i in range(2, n):
        if i**2 >= n:
            break
        if n % i == 0:
            return False
    return True
