def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    arr = [24, 12, 45, 2, 10]
    bubbleSort(arr)
    print("Sorted array :" , arr)
