def func(li, n):

    if(n%2 != 0):
        odd_middle_ele = (n//2 + 1)
        return(odd_middle_ele)

    elif(n%2 == 0):
        i = (n//2)
        j = (i-1)

        ans = (li[i] + li[j])//2
        return ans

n = int(input())
li = [int(x) for x in input().split()]

ans = func(li,n)
print(ans)