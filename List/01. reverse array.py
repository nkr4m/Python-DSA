def reverse_func(li, n):
    for i in li[::-1]:
        print(i, end=" ")

n = int(input())
li = [int(x) for x in input().split()]

reverse_func(li, n)