address = ['https://blog.naver.com/1' , 'https://blog.naver.com/s_eun2/2228' ,
           'https://photohistory.tistory.com/abc' , 'https://photohistory.tistory.com/fact']

word = input("어떤 단어를 찾겠습니까?")

for i in address:
    if word in i:
        print(i)