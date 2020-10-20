li = [1,1,2,2,3,4,5,6, 6, 9999 ,9999]
li2 = []

for ele in range(n):
    if(ele < max(li)):
        li2.append(ele)

print(max(li2))