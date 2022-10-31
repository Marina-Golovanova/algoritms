a, b, c, d = [int(i) for i in input().split()]


def f3(x):
    return a * (x**3) + b * (x**2) + c * x + d


r = 1

while f3(r) * f3(-r) > 0:
    r *= 2

l = -r
e = 1e-4

while (r - l) > e:
    m = (r + l) / 2
    if f3(m) == 0:
        break
    elif f3(m) * f3(r) > 0:
        r = m
    else:
        l = m

print((l + r) / 2)
