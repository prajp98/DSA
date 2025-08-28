def linearSearch(arr, target):
    n=len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr=[1, 30, 28, 15, 6, 10]
    x = 10
    res = linearSearch(arr,x)
    if(res == -1):
        print("Element is not present in the array")
    else:
        print("Element found at index ",res)