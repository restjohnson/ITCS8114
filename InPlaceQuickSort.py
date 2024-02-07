import random


def partition(numbers: [], i: int, j: int):
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

    p = partition(numbers, i, j)

    quick_sort(numbers, i, p)
    quick_sort(numbers, p + 1, j)




def main():
    numbers = []
    length = int(input("Enter the length of the array: "))
    while len(numbers) < length:
        digits = random.randint(0, length*100)
        numbers.append(digits)
    print()

    print("The Unsorted List: ")
    print(numbers)
    print()
    quick_sort(numbers, 0, len(numbers)-1)
    print("The Sorted List:")
    print(numbers)


main()


