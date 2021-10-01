for t in range(int(input())):
    a = input() + 'z'
    b = input() + 'z'

    pointer1, pointer2 = 0, 0
    finalString = []

    while pointer1 < len(a) and pointer2<len(b):
        if a[pointer1] < b[pointer2]:
            finalString.append(a[pointer1])
            pointer1 += 1

        elif a[pointer1] > b[pointer2]:
            finalString.append(b[pointer2])
            pointer2 += 1
