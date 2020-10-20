def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j += 1
        else:
            print(arr2[j], end=" ")
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i], end=" ")
        i += 1

    while j < n:
        print(arr2[j], end=" ")
        j += 1


# Driver program to test above function
m = int(input())
arr1 =  [int(x) for x in input().split()]
n = int(input())
arr2 = [int(x) for x in input().split()]
printUnion(arr1, arr2, m, n)