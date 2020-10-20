def func(li):
    total_sum = max_sum = li[0]

    for i in li[1:]:
        total_sum = max(i, total_sum + i)
        max_sum = max(max_sum, total_sum)

    return max_sum  

n = int(input())
li = [int(x) for x in input().split()]

ans = func(li)
print(ans)