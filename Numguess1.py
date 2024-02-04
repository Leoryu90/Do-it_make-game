import random

userInput = ""
userGuess = 0

randNum = random.randrange(1,101)

print("1 부터 100 중에 숫자를 정했습니다.\n이 숫자는 무엇일까요?")

while randNum != userGuess:
    userInput = input("예상 숫자: ").strip()
    if not userInput.isnumeric():
        print(userInput, "이것은 숫자가 아닙니다.")
    
    else:
        userGuess = int(userInput)
        if userGuess < randNum:
            print("당신의 숫자가 작습니다. 다시입력하세요.")
        elif userGuess > randNum:
            print("당신의 숫자가 큽니다. 다시입력하세요.")
        else:
            print("정답입니다.")

print("잘 맞춰보셨나요? 다음에 다시 해주세요.")