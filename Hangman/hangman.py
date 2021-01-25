import random
import re

# Write your code here
print("H A N G M A N")
print()
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hint = ['-'] * len(word)
NOT_END = True
n_try = 7
tried_letters = set()
play = False
while not play:
    a = input("Type \"play\" to play the game, \"exit\" to quit:")
    if a == "play":
        play = True
    elif a == "exit":
        break
    else:
        continue

while NOT_END and play:
    print("".join(hint))

    letter = input("Input a letter:")

    if len(letter) != 1:
        print("You should input a single letter")
    elif not letter.islower():
        print("Please enter a lowercase English letter")
    elif letter in tried_letters:
        print("You've already guessed this letter")
    elif letter in word:
        appear = [m.start() for m in re.finditer(letter, word)]
        for i in appear:
            hint[i] = letter
    else:
        print(f"That letter doesn't appear in the word\nLives:{n_try}/8")
        n_try -= 1
    if n_try < 0:
        print("You lost!")
        break
    if "-" not in hint:
        print(f"""You guessed the word {"".join(hint)}!\nYou survived!""")
        break
    tried_letters.add(letter)
    print()
