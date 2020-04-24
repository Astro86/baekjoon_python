n = int(input())


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

    def __init__(self, list):
        self.name = list[0]
        self.day = int(list[1])
        self.month = int(list[2])
        self.year = int(list[3])

    def __lt__(self, student):
        if(self.year == student.year):
            if(self.month == student.month):
                return self.day < student.day
            return self.month < student.month
        return self.year < student.year

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
