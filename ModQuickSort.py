import InsertSort
import random


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
        InsertSort.insert_sort(arr)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    length = int(input("Enter the integer length of the array: "))
    array = [random.randint(0, length*100) for i in range(length)]
    print("The Unsorted List is: ")
    print(array)
    print()
    print("The Sorted List is: ")
    quick_sort(array)
    print(array)



