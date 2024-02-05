asciiMin = 32
asciiMax = 126

key = 3141592
key = str(key)

action = input("암호화(E) 또는 복호화(D) 중에서 E 또는 D를 입력하세요.")

if action == "E" or "e":

    message = input("암호화할 메시지를 입력하세요 : ")

    messEncr = ""

    for index in range(0, len(message)):
        char = ord(message[index])
        if char < asciiMin or char > asciiMax:
            messEncr += message[index]
        else:
            ascNum = char + int(key[index % len(key)])
            if ascNum > asciiMax:
                ascNum -= (asciiMax - asciiMin)
        
            messEncr = messEncr + chr(ascNum)

    print("암호화한 메세지 : ", messEncr)

elif action == "D" or "d":

    message = input("복호화할 글자를 입력하세요 : ")

    messEncr = ""

    for index in range(0, len(message)):
        char = ord(message[index])
        if char < asciiMin or char > asciiMax:
            messEncr += message[index]
        else:
            ascNum = char - int(key[index % len(key)])
            if ascNum < asciiMin:
                ascNum += (asciiMax - asciiMin)
        
            messEncr = messEncr + chr(ascNum)

    print("암호화한 메세지 : ", messEncr)
