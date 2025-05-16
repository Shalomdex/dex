import json
import random
import os

# File path for the questions JSON file
file_path = "/home/shalomadejobi/Python Project/questions.json"

def load_questions(file_path):
    """Load quiz questions from a JSON file."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
    
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
            return questions
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file.")
        return []

def quiz_game():
    """Run the CLI quiz game."""
    questions = load_questions(file_path)

    if not questions:
        print("No questions available. Exiting game.")
        return

    # Randomize the order of questions
    random.shuffle(questions)

    score = 0
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question['question']}")
        
        # Randomize answer options
        answers = question['choices']
        correct_answer = question['answer']
        random.shuffle(answers)

        # Display options
        for i, option in enumerate(answers):
            print(f"{i + 1}. {option}")

        # Get user's answer
        while True:
            try:
                user_choice = int(input("Enter your choice (1-4): "))
                if 1 <= user_choice <= len(answers):
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a number between 1 and 4.")

        # Check if the answer is correct
        if answers[user_choice - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")

    # Display final score
    print("\nQuiz Over!")
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
