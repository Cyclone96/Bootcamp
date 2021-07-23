import random

input("Welcome to Rock, Paper, Scissors. Press Enter to start. ")

user_score = 0
cpu_score = 0

while True:
	print()
	user_choice = input("Rock, Paper or Scissors? ").lower()
	while user_choice!= "rock" and user_choice != "paper" and user_choice != "scissors":
		user_choice = input("Invalid choice! Please try again:").lower()


	random_num = random.randint(0, 2)
	if random_num == 0:
		cpu_choice = "rock"
	elif random_num == 1:
		cpu_choice = "paper"
	elif random_num == 2:
		cpu_choice = "scissors"

	print()
	print("Your Choice:",user_choice)
	print("Computer's choice:", cpu_choice)
	print()

	if user_choice == "rock":
		if cpu_choice == "rock":
			print("Iish! It's a tie!")
		elif cpu_choice == "paper":
			print("Dang! You lost!")
			cpu_score += 1
		elif cpu_choice == "scissors":
			print("Yaay! You Win!!!")
			user_score += 1

	elif user_choice == "paper":
		if cpu_choice == "paper":
			print("Iish! It's a tie!")
		elif cpu_choice == "scissors":
			print("Dang! You lost!")
			cpu_score += 1
		elif cpu_choice == "rock":
			print("Yaay! You Win!!!")
			user_score += 1
	elif user_choice == "scissors":
		if cpu_choice == "scissors":
			print("Iish! It's a tie!")
		elif cpu_choice == "rock":
			print("Dang! You lost!")
			cpu_score += 1
		elif cpu_choice == "paper":
			print("Yaay! You Win!!!")
			user_score += 1

	print("You have", user_score, "points")
	print("The computer has", cpu_score, "points")
	print()

	repeat = input("Wanna Play Again? (Y/N)").lower()
	while repeat != "n" and repeat != "y":
		repeat = input("Invalid input! Please try again: ").lower()

	if repeat == "n":
		break	

	print("\n---------------------\n")
