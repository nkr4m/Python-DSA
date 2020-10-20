def fact(n):
    if(n == 0):
        return 1

    return n * fact(n-1)

a = int(input())

for i in range(a):
    n = int(input())
    ans = fact(n)
    print(ans)