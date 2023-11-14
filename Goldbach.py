def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_partition(even_number):
    if even_number < 4 or even_number % 2 != 0:
        return None  # Goldbach's conjecture applies to even numbers greater than 2

    for i in range(2, even_number // 2 + 1):
        if is_prime(i) and is_prime(even_number - i):
            return i, even_number - i

# Example
even_number = 18
result = goldbach_partition(even_number)
if result:
    print(f"{even_number} = {result[0]} + {result[1]}")
else:
    print(f"The Goldbach Conjecture doesn't apply to {even_number}.")
