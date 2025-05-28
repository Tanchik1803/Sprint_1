list = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = list.split(',')

count_minute = 0

for time in time_list:
    time = time.replace(' ','')
    h = 0
    m = 0
    s = 0
    if 'h' in time:
        h = int(time[:time.index('h')])
        time = time[time.index('h')+1:]
    if 'm' in time:
        m = int(time[:time.index('m')])
        time = time[time.index('m')+1:]
    if 's' in time:
        s = int(time[:time.index('s')])
    count_minute += h*60+m+s/60

print(int(count_minute))
