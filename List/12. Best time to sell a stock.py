def func(li):

    temp = 0
    max_temp = 0

    for i in range(1,n-2,1):
        if ((li[i+1] - li[i]) >= 0):
            temp = (li[i+1] - li[i])
            max_temp = max(temp, max_temp)
    return max_temp

n = int(input())
li = [int(x) for x in input().split()]

ans = func(li)

if ans == 0:
    print('0')

for i in range(0,n-1,1):
    if (ans == (li[i+1] - li[i])):
        print(li[i+1])