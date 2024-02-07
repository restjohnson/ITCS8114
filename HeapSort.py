import random


def heapify(arr: list, n, i):
    largest = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    length = int(input("Enter the length of the array: "))
    array = [random.randint(0, length*100) for i in range(length)]
    print("The Unsorted List is: ")
    print(array)
    print()
    print("The Sorted List is: ")
    print(heap_sort(array))




