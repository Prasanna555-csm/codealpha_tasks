import random
words = ["clanguage", "java", "javascript", "python", "html", "css"]
word = random.choice(words)
guessed_letters = []
attempts = 6
hangman = [
'''
 +---+
 |   |
     |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
'''
]
print("================================")
print("       HANGMAN GAME")
print("================================")
while attempts > 0:
    print(hangman[6 - attempts])
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    if "_" not in display_word:
        print("\n🎉 CONGRATULATIONS! YOU WIN!")
        print("The word was:", word)
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet.")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Attempts Left:", attempts)
if attempts == 0:
    print(hangman[6])
    print("\n💀 GAME OVER! YOU LOSE!")
    print("The word was:", word)
    