# It needs to get random imported
import random


# Lottery App

def menu():
# Asks the player for numbers.
    user_numbers = get_player_numbers()
# Calculate lottery numbers.
    lottery_numbers = create_lottery_numbers()
# Print out the winnings.
    matching_numbers = user_numbers.intersection(lottery_numbers)
# In this app the winnings is a multiplicative of the findings, being the least win of 1 dollar and a maximum of $1000000000000.
    print("You matched {}. You won ${}!".format(matching_numbers, 100 ** len(matching_numbers)))


# The user gets to pick 6 numbers.
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by comas: ")
# Now, i want to create a set of integers from this number_csv.
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set


# This lottery app calculates 6 random numbers (between 1 and 30) (in this case).
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 30))
    return values


menu()
