
asciiMin = 32
asciiMax = 126

key = 3141592
key = str(key)

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