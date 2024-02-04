currGuess = input("추측문자: ").strip().lower()

if len(currGuess) > 1:
    currGuess = currGuess[0]

print(currGuess)