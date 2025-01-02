# Write a program where the computer generates a random number, and the user tries to guess it.
import random
def main():

    # get user input
    guess = int(input("Try and guess the randomly generated number between 1-10: "))


    # generate random number
    my_list = [1, 10]
    random_number = random.choice(my_list)

    print(f"You guessed {guess} the generated number was {random_number}.")


    # congratulate user
    if guess == random_number:
        print("Congrats you guessed correctly!!")
    else:
        print("you suck")


main()
