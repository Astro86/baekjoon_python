cnt_hour, cnt_minute, cnt_second = list(map(int, input().split(':')))
start_hour, start_minute, start_secode = list(map(int, input().split(':')))

if(start_secode < cnt_second):
    start_secode += 60
    start_minute -= 1

if(start_minute < cnt_minute):
    start_minute += 60
    start_hour -= 1

if(start_hour < cnt_hour):
    start_hour += 24


def make2word(value):
    if(0 <= value <= 9):
        return '0'+str(value)
    else:
        return str(value)


h = start_hour - cnt_hour
m = start_minute - cnt_minute
s = start_secode - cnt_second
print(f'{h:02}:{m:02}:{s:02}')
