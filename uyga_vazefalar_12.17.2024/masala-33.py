a = [1,2,3,4,5,6,7,2, 8]
b = [1,3,4,56,66,5,9]
ikkilar = []
s=0
for i in [a,b]:
    s=0
    for j in range(len(i)):
        if 2 == i[j]:
            s += 1

            ikkilar.append(j)
            son = len(ikkilar)


print(ikkilar[son-1])

if s == 0 :
    print(0)



