def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

if __name__ == '__main__':
    arr = [24, 12, 45, 2, 10]
    selectionSort(arr)
    print("Sorted array :" , arr)
