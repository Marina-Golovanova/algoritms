# найти минимальный элемент
# поставить его в начало
# на следующем этапе ищем минимальный элемент среди оставшихся
# меняем с первым элементов в неотсортированной части

arr = [2, 1, 6, 4, 8, 0]


def selection_sort(arr):
    for i in range(len(arr)):
        min_inx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_inx]:
                min_inx = j
        arr[i], arr[min_inx] = arr[min_inx], arr[i]


selection_sort(arr)
print(arr)
