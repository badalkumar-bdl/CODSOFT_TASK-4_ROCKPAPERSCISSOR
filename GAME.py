import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors ---")
    print(f"Score - You: {user_score}, Computer: {computer_score}")
    
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        continue
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        break

print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
print("Thanks for playing!")