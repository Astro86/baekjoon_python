n = int(input())

for i in range(n):
    arr = {}
    m = int(input())
    for j in range(m):
        price, name = input().split()
        arr[int(price)] = name

    print(arr[max(arr)])
