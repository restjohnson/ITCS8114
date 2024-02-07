


import random


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


def main():
    length = int(input("Enter the length of the array:"))
    numbers = [random.randint(0, length * 100) for i in range(length)]
    while len(numbers) < length:
        digits = random.randint(1, length*50)
        numbers.append(digits)

    print("The Unsorted List is:")
    print(numbers)
    merge_sort(numbers)
    print("The Sorted List is:")
    print(numbers)


main()



