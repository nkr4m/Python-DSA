def func(li, li2, n, m):
    i = 0
    j = 0

    while(i<n and j<m):
        if(li[i] < li2[j]):
            print(li[i],end=" ")
            i = i + 1
        elif(li2[j] < li[i]):
            print(li2[j], end=" ")
            j = j + 1

    while(i<n):
        print(li[i],end=" ")
        i = i + 1

    while(j<m):
        print(li2[j],end=" ")
        j = j + 1



n = int(input())
li = [int(x) for x in input().split()]
m = int(input())
li2 = [int(a) for a in input().split()]

func(li, li2, n, m)