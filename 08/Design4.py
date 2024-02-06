"""
guessLetters = []

for i in range (0, 5):
    currGuess = input("추측문자: ").strip().lower()
    if len(currGuess) > 1:
        guessLetters.append(currGuess[0])
    else:
        guessLetters.append(currGuess)

guessLetters.sort()

#print(guessLetters)

youTried = ""

for letter in guessLetters:
    youTried += letter

print("시도한 문자: " + str(youTried))
"""

gameWord = "apocalypse"
guessedLetters = []
maskChar = "_"

displayWord = maskChar * len(gameWord)

for letter in gameWord:    
    if letter in guessedLetters:
        displayWord += letter
    else:
        displayWord += maskChar

print("원래 단어: ", gameWord)
print("마스킹한 단어: ", displayWord)