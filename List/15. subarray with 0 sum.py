def func(li):
    sum_must_be = 0
    sub_array_total = li[0]
    length = len(li) - 1

    for i in li[1:length:1]:
        sub_array_total = sub_array_total + li[i]
        if(li[i] == sum_must_be):
            return True
        if(sub_array_total == sum_must_be):
            return True

    return False


n = int(input())
li = [int(x) for x in input().split()]
ans = func(li)

if ans:
    print("True")
else:
    print('False')