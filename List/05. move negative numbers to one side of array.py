def rearrange(arr, n):

    j = 0
    for i in range(0, n, 1):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    print(arr)


# Driver code
n = int(input())
arr = [int(x) for x in input().split() ]
rearrange(arr, n)