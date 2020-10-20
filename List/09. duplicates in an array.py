def func(li):
    for i in range(0,n,1):
        for j in range(0,n,1):
            if(li[i] == li[j] and i != j):
                return li[i]


n = int(input())
li = [int(x) for x in input().split()]

ans = func(li)
print(ans)