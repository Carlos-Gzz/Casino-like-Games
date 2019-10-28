# Another fun fast casino-like game
# In this mini-game, we are also using the random feature.
import random

# In here we get 2 choices out of 9 (in this case).
def ask_user_and_check_nummber():
    user_number = int(input("Enter a number between 0 and 9: "))
    x = random.randint(0, 9)
    magic_numbers = [x, x]
    if user_number in magic_numbers:
        return "You got it right"
    else:
        return "Your got it wrong"


# Here we can make this little game be played several different times.
def run_program_x_times(chances):
# Here I tell the user the attempt number, to keep him/her intrigued in the game.
    for attempt in range(chances):
        print("This is attempt {}".format(attempt + 1))
        message = ask_user_and_check_nummber()
        print(message)


user_attempts = int(input("Enter the number of attempts: "))
run_program_x_times(user_attempts)
