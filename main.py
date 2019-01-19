number = "4"
guess = ""
count = 0
max_guesses = False

while guess != number and not max_guesses:
    if count < 3:
        guess = input("enter number: ")
        count += 1

    else:
        max_guesses = True

if max_guesses:
    print("Sorry, try again")

else:
    print("you win")
