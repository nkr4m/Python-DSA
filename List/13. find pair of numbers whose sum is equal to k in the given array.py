def func(li, k):
    count = 0
    for i in range(0, n, 1):
        for j in range(1,n-1,1):
            if(li[i] + li[j] == k and i != k):
                count = count + 1
    return count



n = int(input())
li = [int(x) for x in input().split()]
k = int(input())

ans = func(li, k)
print(ans)