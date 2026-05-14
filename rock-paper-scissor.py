import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    
    # Logic: Rock beats scissors, scissors beat paper, paper beats rock
    win_conditions = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if win_conditions[user] == computer:
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    
    print("================================")
    print("   ROCK, PAPER, SCISSORS!")
    print("================================")
    print("Instructions: Type 'rock', 'paper', or 'scissors'.")
    print("To quit the game, type 'exit'.")

    while True:
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
        user_choice = input("Your choice: ").lower().strip()

        if user_choice == 'exit':
            print("\nFinal Result:")
            print(f"You: {user_score} - Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("!! Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print(">> It's a tie!")
        elif result == "user":
            print(f">> You win! {user_choice.capitalize()} beats {computer_choice}.")
            user_score += 1
        else:
            print(f">> You lose! {computer_choice.capitalize()} beats {user_choice}.")
            computer_score += 1

        # Play again prompt
        play_again = input("\nPlay another round? (y/n): ").lower().strip()
        if play_again != 'y':
            print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()