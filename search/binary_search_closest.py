# если два ближайших элемента, выводится меньший

def binary_search_closest(arr, k):
    l = -1
    r = len(arr)

    while r > l + 1:
        m = (r + l) // 2
        if arr[m] <= k:
            l = m
        elif arr[m] > k:
            r = m
    if l < 0:
        return arr[r]
    elif r == len(arr):
        return arr[l]
    elif arr[r] - k >= k - arr[l]:
        return arr[l]
    return arr[r]


arr = [1, 3, 5, 6, 7, 8, 9]
searching_el = [2, 5, 4, 8, 11]
for el in searching_el:
    print(binary_search_closest(arr, el))
