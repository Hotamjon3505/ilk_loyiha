a = [1,2,3,4,5,6,7,8]
b = [1,3,4,56,66,5,9]

s=0
for i in [a,b]:
    for j in range(len(i)):
        if 2 == i[j]:
            print(j)
            s += 1
if s != 0 :
    print(0)


