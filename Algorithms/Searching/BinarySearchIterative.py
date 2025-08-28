def binarySearch(arr, target):
    l = 0
    r = len(arr) - 1

    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == '__main__':
    arr = [2, 6, 7, 10, 19, 100]
    x = 10
    res = binarySearch(arr, x)
    if res==-1:
        print("Element is not present in the array")
    else:
        print("Element found at index ", res)