def cyclic(arr, n):

    x = arr[n - 1]
    for i in range(n -1 , 0, -1):
        arr[i] = arr[i - 1]
    print(li)




n = int(input())
li = [int(x) for x in input().split()]
cyclic(li, n)