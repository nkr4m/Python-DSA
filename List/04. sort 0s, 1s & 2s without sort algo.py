def sort012(li, n):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for ele in li:
        if(ele == 0):
            count_0 += 1
        elif(ele == 1):
            count_1 += 1
        elif(ele == 2):
            count_2 += 1

    i = 0
    while(count_0 > 0):
        li[i] = 0
        i += 1
        count_0 -= 1

    while (count_1 > 0):
        li[i] = 1
        i += 1
        count_1 -= 1

    while (count_2 > 0):
        li[i] = 2
        i += 1
        count_2 -= 1

    return li


n = int(input())
li = [int(x) for x in input().split()]
ans = sort012(li, n)

print(li)