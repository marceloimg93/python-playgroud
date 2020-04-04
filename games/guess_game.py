# only works on python3.7

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!!!")