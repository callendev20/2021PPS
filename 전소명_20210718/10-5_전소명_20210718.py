def solution(a, b):
    answer = ''
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    dateOfYear = sum(dates[:a-1])+b
    print(dateOfYear)
    answer = day[dateOfYear%7-1]
    print(answer)
    return answer