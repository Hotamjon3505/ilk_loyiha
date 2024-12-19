
n = int(input("N (butun sonlar soni) ni kiriting: "))
k = int(input("K (to'plamlar soni) ni kiriting: "))

count = 0
for _ in range(k):

    elements = list(map(int, input("To'plamni kiriting (bo'sh joy bilan ajrating): ").split()))

    element_count = {}

    for number in elements:
        if number in element_count:
            element_count[number] += 1
        else:
            element_count[number] = 1

    for count in element_count.values():
        if count >= 2:
            count += 1
            break

print("2 yoki undan ko'p bo'lgan to'plamlar soni:", count)
