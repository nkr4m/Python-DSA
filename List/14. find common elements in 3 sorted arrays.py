def func(li, li2, li3):
    for i in range(0, len(li), 1):
        for j in range(0, len(li2), 1):
            for k in range(0, len(li3), 1):
                if(li[i] == li2[j] == li3[k]):
                    print(li[i],end=" ")


n = int(input())
li = [int(x) for x in input().split()]
m = int(input())
li2 = [int(x) for x in input().split()]
k = int(input())
li3 = [int(x) for x in input().split()]

func(li, li2, li3)