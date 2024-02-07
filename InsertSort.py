import random


def insert_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    length = int(input("Enter the integer length of the array: "))
    array = [random.randint(0, length*100) for i in range(length)]
    print("The Unsorted List is: ")
    print(array)
    print()
    print("The Sorted List is: ")
    insert_sort(array)
    print(array)