#라이브러리 호출
import datetime

today = datetime.datetime.now()

#if today.weekday() == 6 or today.weekday() == 5:
# or 은 둘중 하나라도 포함이면
if today.weekday() in [5,6]:
    print("오늘은 주말입니다.\n코딩 공부를 하루종일 할 수 있습니다.")

elif today.weekday() == 4:
    print("오늘은 금요일입니다.")
    print("저녁에 공부가 가능합니다.")

else:
    print("일이나 열심히 하세요")