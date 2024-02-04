import random

guesses = 0
numMin = 0
numMax = 0
userInput = ""
userGuess = 0

numMin = int(input("최소 숫자를 입력해 주세요."))
numMax = int(input("최대 숫자를 입력해 주세요."))

print(numMin, "부터", numMax, "까지 숫자를 정했습니다.\n이 숫자는 무엇일까요?")

randNum = random.randrange(numMin, numMax + 1)

while randNum != userGuess:
    userInput = input("예상 숫자: ").strip()
    if not userInput.isnumeric():
        print(userInput, "이것은 숫자가 아닙니다.")
    
    else:
        guesses = guesses + 1
        userGuess = int(userInput)
        if userGuess < randNum:
            print("당신의 숫자가 작습니다. 다시입력하세요.")
        elif userGuess > randNum:
            print("당신의 숫자가 큽니다. 다시입력하세요.")
        else:
            print("정답입니다. 당신은", guesses, "번 만에 성공했습니다.")

print("잘 맞춰보셨나요? 다음에 다시 해주세요.")