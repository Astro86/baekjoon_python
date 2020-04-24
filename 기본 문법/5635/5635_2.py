n = int(input())

people = {}
for i in range(n):
    data = input().split()
    people[data[0]] = [int(data[3]), int(data[2]), int(data[1])]

# Value를 이용한 dictionary 정렬하기
s = sorted(people.items(), key=lambda k: (k[1][0], k[1][1], k[1][2]))

print(s[-1][0])
print(s[0][0])
