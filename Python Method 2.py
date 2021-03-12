import itertools
import math


res = []
up = 1.1
down = 0.909


def factorials(m, n):
    r = 1
    for v in range(m, n):
        r *= v
    return r


def constitute(r, n):
    if r > (n / 2):
        u = factorials(r + 1, n + 1)
        d = factorials(1, n - r + 1)
        if d == 0:
            return 1
        return u / d
    else:
        u = factorials(n - r + 1, n + 1)
        d = factorials(1, r + 1)
        if d == 0:
            return 1
        return u / d


def call_option():
    print("Call Option:")
    print(f'{"t":10}{"V":10}')
    for i in range(53):
        total = 0
        for k in range(int(i / 2) + 1):
            c = constitute(k, i)
            total += c * (math.pow(up, i - k) * math.pow(down, k) - 1) * math.pow(0.5, i)
        print(f'{i:<10}', end=' ')
        print(f"{f'{total:.4g}':10}")
    print("The price:")
    print(f'{50 * total:2.4g}')
    result = 0.00
    for i in range(53):
        if math.pow(up, i) - 1 > total:
            result = math.pow(up, i)
            break
	result *= 4
    print(f'When the unit price of oil is greater than or equal to ${result:1.3g}, the right can be exercised.')


def put_option():
    print("Put Option:")
    print(f'{"t":10}{"V":10}')
    for i in range(53):
        total = 0
        for k in range(int(i / 2) + 1):
            c = constitute(k, i)
            total += c * (1 - math.pow(up, k) * math.pow(down, i - k)) * math.pow(0.5, i)
        print(f'{i:<10}', end=' ')
        print(f"{f'{total:.4g}':10}")
    print("The price:")
    print(f'{50000 * total:4.6g}')
    result = 0.00
    for i in range(53):
        if 1 - math.pow(down, i) > total:
            result = math.pow(down, i)
            break
	result *= 4
    print(f'When the unit price of oil is less than or equal to ${result:.2g}, the right can be exercised.')


call_option()
put_option()
