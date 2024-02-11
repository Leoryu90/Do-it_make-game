import datetime

#year = input("당신이 태어난 해는 언제인가요?")
#year = int(year)
year = int(input("당신이 태어난 해는 언제인가요?"))
month = input("당신이 태어난 달은 언제인가요?")
month = int(month)
day = input("당신이 태어난 날은 언제인가요?")
day = int(day)

bday = datetime.datetime(year, month, day)

if bday.weekday() == 6:
#    print("당신이 태어난 날은 일요일입니다.")
    dow = "일"
elif bday.weekday() == 0:
#    print("당신이 태어난 날은 월요일입니다.")
    dow = "월"
elif bday.weekday() == 1:
#    print("당신이 태어난 날은 화요일입니다.")
    dow = "화"
elif bday.weekday() == 2:
#    print("당신이 태어난 날은 수요일입니다.")
    dow = "수"
elif bday.weekday() == 3:
#    print("당신이 태어난 날은 목요일입니다.")
    dow = "목"
elif bday.weekday() == 4:
#    print("당신이 태어난 날은 금요일입니다.")
    dow = "금"
elif bday.weekday() == 5:
#    print("당신이 태어난 날은 토요일입니다.")
    dow = "토"

print("당신이 태어난 요일은", dow + "요일 입니다.")