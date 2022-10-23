arr = [2, 1, 0, 2, 4, 5]


def counting_sort(arr):
    min_el = min(arr)
    max_el = max(arr)

    counts = [0] * (max_el - min_el + 1)

    for el in arr:
        counts[el - min_el] += 1

    index = 0
    for i in range(len(counts)):
        for _ in range(counts[i]):
            arr[index] = i + min_el
            index += 1

    return None


counting_sort(arr)
print(arr)
