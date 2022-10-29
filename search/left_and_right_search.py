arr = [int(i) for i in input().split()]
arr_m = [int(i) for i in input().split()]

bounds = {}

i = 0

while i < len(arr):
    l = i
    r = i
    while r < len(arr) and arr[r] == arr[i]:
        r += 1

    bounds[arr[i]] = [l, r - 1]
    i = r

for el in arr_m:
    if el in bounds:
        print(el)
    else:
        print(0)
