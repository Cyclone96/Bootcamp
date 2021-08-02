import random
number = random.randint(1, 10)

player_name = input("State your name: ")
number_of_guesses = 0
print('Hola '+ player_name+ ' Guess any number between 1 to 10:')
print()

def game():
    number = random.randint(1, 10)
    print("You got five guesses to make starting now....!")
    i = 1
    r = 1
    while i<6:  
        user_number = int(input('Enter your number: ')) 
        if user_number < number:
            print("Your guess is too low")
            print()
            print("You now have " + str(5-i)+ " chances left" )
            i = i+1
        elif user_number > number:
            print("Your guess is too high")
            print()
            print("You now have " + str(5-i)+ " chances left" )
            i = i+1
        elif user_number == number:
            print("\nYou have guessed the correct number!")
            print("Yaaay! Keep going!!! :)")
            r = 0;
            break
        else:
            print("Invalid Choice")
            print("You have " + str(5-i)+ " chances left" )
            continue
    if r==1:
        print("Dang!!! You lost!!")
        print()
        print("My choice was = " + str(number))
        print("Try again next round!")

def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break
main()
print("\nThe End! Thanks for coming :)")