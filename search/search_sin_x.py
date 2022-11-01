a = float(input())


def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def getSummand(x, k):
    power = k * 2 + 1
    numerator = x**power
    denominator = fact(power)
    sign = -1 if k % 2 == 1 else 1

    return numerator / denominator * sign


def sin(x):
    e = 1e-5

    summand = getSummand(x, 0)
    s = summand
    i = 1

    while abs(summand) > e:
        summand = getSummand(x, i)
        s += summand
        i += 1

    return s


l = -3.14 / 2
r = 3.14 / 2
e = 1e-5

while r - l > e:
    m = (r + l) / 2
    if sin(m) > a:
        r = m
    else:
        l = m

print((r + l) / 2)
