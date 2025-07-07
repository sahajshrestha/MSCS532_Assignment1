def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

if __name__ == "__main__":
    data = [9, 13, 7, 21, 4]
    print("Given Unsorted Array:", data)
    insertion_sort_descending(data)
    print("Sorted In Descending Order:", data)
