def binarySearch(arr, l, r, target):
    if l > r:
        return -1
    mid = (l + r) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearch(arr, mid + 1, r, target)
    else:
        return binarySearch(arr, l, mid-1, target)

if __name__ == '__main__':
    arr = [2, 6, 7, 10, 19, 100]
    x = 10
    res = binarySearch(arr,0, len(arr)-1, x)
    if res==-1:
        print("Element is not present in the array")
    else:
        print("Element found at index ", res)