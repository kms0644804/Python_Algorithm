'''
1. 5명 모여야 하니까 9시까지 가도 됨
2. 2명 모이는데 10분 간격으로 2번 온다 09:10분은 셔틀을 못타고 탈ㄹ려면 9:09에 도착해야 선착순으로 탈수있다
3. 1분간격으로 2번 오지만 선착순에서 밀리지 않으려면 더 빨리와야함
4. 선착순으로 밀리지 않고 5명 타는 버스를 타려면 일찍와야함
5. 그냥 9시에 타면 선착순임
6. 9시부터 1시간씩 10번(9시 포함) -> 18시가 마지막, 그리고 선착순에 밀리지 않음
9 10 11 12 13 14 15 16 17 18
'''

n = 10
t = 60
m = 45
#timetable = ["08:59", "08:01", "08:02", "09:03"]
#timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
#timetable = ["08:57", "08:54", "08:55", "09:00"]
#timetable = ["09:10", "09:09", "08:00"]
timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

'''
고려할 요소
버스는 9시부터 온다
버스가 다시 오는 시간이 있는지 확인 n
다음 버스가 언제 오는지 확인 t
버스를 탈 자리가 되는지 확인 m
선착순에서 밀리지는 않는지 확인 timetable
'''
def solution(n, t, m, timetable):
    time = "09:00"
    hour = int(time[0:2])
    minu = int(time[3:5])
    time = hour * 100 + minu
    # print("bus_time: ", str(time))
    ttemp = 0
    answer = ""

    arr = []
    for i in range(len(timetable)):
        hour = int(timetable[i][0:2])
        minu = int(timetable[i][3:5])
        temp_time = hour * 100 + minu
        arr.append(temp_time)

    arr.sort()  # timetable을 시간순으로 정렬함
    # print("arr: ", arr)
    if n == 1:  # 무조건 버스는 9시에 온다
        ### 다같이 일찍 올수도 있다다
        ## n이 1이면 t는 의미가 없다
        # timetable의 갯수와 시간, 그리고 남은 자리를 계산해야한다.
        # 자리가 남으니까 가장 늦게 도착하는건 09시
        if arr[0] > 900 or m > len(arr):
            answer = "09:00"
        elif m == len(arr):  # 한자리 먼저 타면 된다. 근데 모두가 같은 시각에 올 수도 있다.
            temp = list(set(arr))
            temp.sort()
            if len(temp) != 1:
                if temp[-1] < 900:
                    if temp[-1] % 100 != 0:
                        ttemp = temp[-1] - 1
                    else:
                        ttemp = temp[-1] - 100 + 59
                    h = int(ttemp / 100)
                    mi = ttemp % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
                elif temp[-1] > 900:
                    answer = "09:00"
                elif temp[-1] == 900:
                    answer = "08:59"
            elif len(temp) == 1:
                if temp[0] > 900:
                    answer = "09:00"
                else:
                    if temp[0] % 100 != 0:
                        ttemp = temp[0] - 1
                    else:
                        ttemp = temp[0] - 100 + 59
                    h = int(ttemp / 100)
                    mi = ttemp % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
        elif m < len(arr):
            if arr[m - 1] > 900:
                answer = "09:00"
            else:
                if arr[m - 1] % 100 != 0:
                    ttemp = arr[m - 1] - 1
                else:
                    ttemp = arr[m - 1] - 100 + 59
                h = int(ttemp / 100)
                mi = ttemp % 100
                answer = '%02d' % h + ":" + '%02d' % mi
    elif n != 1:
        ## n번 만큼 버스가 올 것이고, 그 간격은 t
        ## 최대로 늦게 도착하는 시간은 09:00 부터 t*(n-1) 만큼 흐른 시간
        times = []
        for i in range(n):
            cnt = 900
            if i * t >= 60:
                cnt += int((i * t) / 60) * 100
            nam = (i * t) % 60
            times.append(cnt + nam)
        # print(times)
        if arr[0] > times[-1]:
            h = int(times[-1] / 100)
            mi = times[-1] % 100
            answer = '%02d' % h + ":" + '%02d' % mi
        elif m * n == len(arr):  # 한 명보다 빨리 가기
            ## 사람들이 다 늦어서 인원이 다 차지 않아도 출발하는 경우는???
            temp = list(set(arr))
            temp.sort()
            # print("temp: ", temp)
            if len(temp) != 1:
                if temp[-1] < times[0]:
                    if temp[-1] % 100 != 0:
                        ttemp = temp[-1] - 1
                    else:
                        ttemp = temp[-1] - 100 + 59
                    h = int(ttemp / 100)
                    mi = ttemp % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
                elif temp[-1] == times[0]:
                    if times[0] % 100 != 0:
                        ttemp = times[0] - 1
                    else:
                        ttemp = times[0] - 100 + 59
                    h = int(ttemp / 100)
                    mi = ttemp % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
                elif temp[-1] > times[-1]:
                    h = int(times[-1] / 100)
                    mi = times[-1] % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
                elif temp[-1] > times[0] and temp[-1] < times[-1]:
                    if temp[-1] % 100 != 0:
                        ttemp = temp[-1] - 1
                    else:
                        ttemp = temp[-1] - 100 + 59
                    h = int(ttemp / 100)
                    mi = ttemp % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
            elif len(temp) == 1:
                if temp[0] > 900:
                    answer = "09:00"
                else:
                    if temp[0] % 100 != 0:
                        ttemp = temp[0] - 1
                    else:
                        ttemp = temp[0] - 100 + 59
                    h = int(ttemp / 100)
                    mi = ttemp % 100
                    answer = '%02d' % h + ":" + '%02d' % mi
        elif m * n < len(arr):
            if arr[m * n - 1] > times[-1]:
                h = int(times[-1] / 100)
                mi = times[-1] % 100
                answer = '%02d' % h + ":" + '%02d' % mi
            else:
                if arr[m * n - 1] % 100 != 0:
                    ttemp = arr[m * n - 1] - 1
                else:
                    ttemp = arr[m * n - 1] - 100 + 59
                h = int(ttemp / 100)
                mi = ttemp % 100
                answer = '%02d' % h + ":" + '%02d' % mi
        elif m * n > len(arr):
            ## 사람들이 다 늦어서 인원이 다 차지 않아도 출발하는 경우는???
            temp_arr = []
            whole = m * n
            for j in range(n):
                temp_time = times[j]
                if whole == len(arr):
                    temp = list(set(arr))
                    temp.sort()
                    if len(temp) != 1:
                        if temp[-1] < temp_time:
                            if temp[-1] % 100 != 0:
                                ttemp = temp[-1] - 1
                            else:
                                ttemp = temp[-1] - 100 + 59
                            temp_arr.append(ttemp)
                        elif temp[-1] > temp_time:
                            temp_arr.append(temp_time)
                        elif temp[-1] == temp_time:
                            if temp[-1] % 100 != 0:
                                ttemp = temp[-1] - 1
                            else:
                                ttemp = temp[-1] - 100 + 59
                            temp_arr.append(ttemp)
                elif m > len(arr):
                    temp_arr.append(times[j])
                elif whole < len(arr):
                    if arr[whole - 1] > temp_time:
                        temp_arr.append(temp_time)
                    else:
                        if arr[whole - 1] % 100 != 0:
                            ttemp = arr[whole - 1] - 1
                        else:
                            ttemp = arr[whole - 1] - 100 + 59
                        temp_arr.append(ttemp)
                del_list = []
                for i in range(len(arr)):
                    if arr[i] < temp_time:
                        del_list.append(arr[i])
                for i in range(len(del_list)):
                    arr.remove(del_list[i])
                whole -= m
            maxi = max(temp_arr)
            h = int(maxi / 100)
            mi = maxi % 100
            answer = '%02d' % h + ":" + '%02d' % mi
    print(answer)
    return answer

solution(n,t,m,timetable)