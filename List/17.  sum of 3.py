n = int(input())
li = [int(x) for x in input().split()]

for i in range(0, len(li), 1):
    for j in range(i + 1, len(li), 1):
        for k in range(j + 1, len(li), 1):
            if (li[i] + li[j] + li[k] == 0):
                print(li[i], li[j], li[k])