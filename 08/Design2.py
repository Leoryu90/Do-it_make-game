guessLetters = []

for i in range (0, 5):
    currGuess = input("추측문자: ").strip().lower()
    guessLetters.append(currGuess)

guessLetters.sort()

"""
print(guessLetters)
"""

for letter in guessLetters:
    print(letter)
