# 백준 5635 - 생일

## 문제
어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오. 

## 입력
첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.이름이 같거나, 생일이 같은 사람은 없다. 

## 출력
첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다. 

## 전체 소스 코드
```python
n = int(input())

# name 과 생년월일을 저장할 수 있는 class를 짯다.
class student:
    name = ""
    day = 0
    month = 0
    year = 0

    def __init__(self, name, day, month, year):
        self.name = name
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    # list를 입력으로 받는 생성자
    def __init__(self, list):
        self.name = list[0]
        self.day = int(list[1])
        self.month = int(list[2])
        self.year = int(list[3])

    # student클래스에서 < 연산자를 사용하기 위해 연산자 오버로딩을 사용했다.
    def __lt__(self, student):
        if(self.year == student.year):
            if(self.month == student.month):
                return self.day < student.day
            return self.month < student.month
        return self.year < student.year

    # student클래스에서 > 연산자를 사용하기 위해 연산자 오버로딩을 사용했다.
    def __gt__(self, student):
        if(self.year == student.year):
            if(self.month == student.month):
                return self.day > student.day
            return self.month > student.month
        return self.year > student.year


value = input().split()
max_person = student(value)
min_person = student(value)

for i in range(n-1):
    value = input().split()
    temp = student(value)

    if(max_person < temp):
        max_person = temp

    if(min_person > temp):
        min_person = temp


print(max_person.name)
print(min_person.name)
```

## 딕셔너리 정렬을 이용한 방법
```python
n = int(input())

people = {}
for i in range(n):
    data = input().split()
    people[data[0]] = [int(data[3]), int(data[2]), int(data[1])]

# Value를 이용한 dictionary 정렬하기
s = sorted(people.items(), key=lambda k: (k[1][0], k[1][1], k[1][2]))

print(s[-1][0])
print(s[0][0])
```

`key=lambda k: (k[1][0], k[1][1], k[1][2])`에서 `k[0]`에 해당 되는값은 `key`이고, `k[1]`에 해당되는 값은 `value`이다. 정렬 우선 순위를 `year -> month -> day`로 하기 위해서 차래대로 `k[1][0]`, `k[1][1]`, `k[1][2]`를 넘겨주었다.
