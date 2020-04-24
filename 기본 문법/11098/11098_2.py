n = input()
for i in range(int(n)):
    m = int(input())
    maxValue = 0
    maxName = ""

    for j in range(m):
        price, name = input().split()
        price = int(price)
        if(maxValue < price):
            maxValue = price
            maxName = name
    print(maxName)
