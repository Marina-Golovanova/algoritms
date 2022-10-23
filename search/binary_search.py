def binary_search(arr, k):
    l = 0
    r = len(arr) - 1

    while r >= l:
        m = (r + l) // 2

        if k == arr[m]:
            return m
        elif k < arr[m]:
            r = m - 1
        elif k > arr[m]:
            l = m + 1

    return -1


arr = [1, 3, 5, 6, 7, 8, 9]
for el in arr:
    print(el, binary_search(arr, el))
