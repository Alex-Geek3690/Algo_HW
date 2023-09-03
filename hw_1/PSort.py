
# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).


def heapify(array, n, i, reverse = False):
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and ((array[i] < array[left]) if reverse else (array[i] > array[left])):
            largest = left

        if right < n and ((array[largest] < array[right]) if reverse else (array[largest] > array[right])):
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            i = largest
        else:
            break    

def sort_heap(array, reverse = False):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, reverse)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0, reverse)

array = [5, 3, 1, 10, 8, 7, 9, 2, 11, 4]
print("Неотсортированный массив:", array)
sort_heap(array)
print("Отсортированный массив(убывание):", array)
sort_heap(array, reverse=True)
print("Отсортированный массив(возрастание):", array)