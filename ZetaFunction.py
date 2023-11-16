import math

def riemann_zeta(s, terms=1000):
    result = 0.0
    for n in range(1, terms + 1):
        result += 1.0 / (n ** s)
    return result

if __name__ == "__main__":
    s_value = 2.0  # You can change this value to calculate the zeta function for different s
    result = riemann_zeta(s_value)
    print(f"Riemann zeta function at s = {s_value}: {result}")
