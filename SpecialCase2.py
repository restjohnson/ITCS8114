import random
import matplotlib.pyplot as plt
import time


def partition_inplace_quick_sort(numbers: [], i: int, j: int):
    midpoint = int(i + (j - i)/2)
    p = numbers[midpoint]
    done = False
    while not done:
        while numbers[i] < p:
            i += 1

        while p < numbers[j]:
            j -= 1

        if i >= j:
            done = True
        else:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

            i += 1
            j -= 1
    return j


def quick_sort(numbers: [], i, j):
    if i >= j:
        return

    p = partition_inplace_quick_sort(numbers, i, j)
    quick_sort(numbers, i, p)
    quick_sort(numbers, p + 1, j)


def insert_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(numbers):
    if len(numbers) > 1:
        m = int(len(numbers)/2)
        left_array = numbers[:m]
        right_array = numbers[m:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0

        while len(left_array) > i and len(right_array) > j:
            if left_array[i] <= right_array[j]:
                numbers[k] = left_array[i]
                i += 1
            else:
                numbers[k] = right_array[j]
                j += 1
            k += 1

        while len(left_array) > i:
            numbers[k] = left_array[i]
            i += 1
            k += 1
        while len(right_array) > j:
            numbers[k] = right_array[j]
            j += 1
            k += 1


def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high-1] = arr[high-1], arr[mid]
    return arr[high-1]


def quick_sort_helper(arr, low, high):
    if low + 15 <= high:
        pivot = median_of_three(arr, low, high)
        left = low + 1
        right = high - 2
        done = False
        while not done:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            else:
                done = True
        arr[left], arr[high-1] = arr[high-1], arr[left]
        quick_sort_helper(arr, low, left-1)
        quick_sort_helper(arr, left+1, high)
    else:
        insert_sort(arr)


def quick_sort_median_of_three(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


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


def measure_runtime(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    input_sizes = [random.randint(0, 10000) for i in range(5)]
    input_sizes.sort()
    runs = 3
    algorithms = ['Quick Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort Median of Three', 'Heap Sort']
    runtimes = {algorithm: [] for algorithm in algorithms}

    for size in input_sizes:
        print()
        print("Input Size = ", size)
        avg_runtimes = {algorithm: 0 for algorithm in algorithms}
        for _ in range(runs):
            array = [random.randint(0, size * 10) for i in range(size)]
            array.sort()
            array.reverse()
            print("Reversed Array: ", array)
            print()
            arrays = {algorithm: array.copy() for algorithm in algorithms}

            avg_runtimes['Quick Sort'] += measure_runtime(quick_sort, arrays['Quick Sort'], 0,
                                                          len(arrays['Quick Sort']) - 1) / runs
            avg_runtimes['Insertion Sort'] += measure_runtime(insert_sort, arrays['Insertion Sort']) / runs
            avg_runtimes['Merge Sort'] += measure_runtime(merge_sort, arrays['Merge Sort']) / runs
            avg_runtimes['Quick Sort Median of Three'] += measure_runtime(quick_sort_median_of_three,
                                                                          arrays['Quick Sort Median of Three']) / runs
            avg_runtimes['Heap Sort'] += measure_runtime(heap_sort, arrays['Heap Sort']) / runs

        for algorithm in algorithms:
            runtimes[algorithm].append(avg_runtimes[algorithm])

    plt.figure(figsize=(10, 6))
    for algorithm in algorithms:
        plt.plot(input_sizes, runtimes[algorithm], label=algorithm)

    plt.xlabel('Input Size')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
    