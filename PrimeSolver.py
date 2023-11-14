def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]

# Example
limit = 50
result = sieve_of_eratosthenes(limit)
print(result)
