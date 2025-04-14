import random

def rock_paper_scissors():
    print("\n=== Rock-Paper-Scissors Game ===")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
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
            
        print(f"\nScores - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

# Run the game
rock_paper_scissors()