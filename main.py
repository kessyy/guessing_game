guess_number = int("4")
guesses = ""
guess_count = 0
max_guesses = False
name = str(input("Enter your name: "))

print("Well Hello " + name + " I am thinking of a number: can you guess it?")

while guesses != guess_number and not max_guesses:
    if guess_count < 3:
        try:
            guesses = int(input("enter number: "))
        except ValueError:
            print("please input number value")
        guess_count += 1
    else:
        max_guesses = True
if max_guesses:
    print("Oops, try again")

else:
    print("you win")
