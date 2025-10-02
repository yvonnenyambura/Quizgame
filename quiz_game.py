import random
import time

# List of quiz questions
questions = [
    {
        "question": "Which is the longest river in Kenya?",
        "options": ["A. Mara River", "B.Athi River", "C. Tana River", "D.Ewaso Ngi'"],
        "answer": "C"
    },
    {
        "question": "In which year did Kenya gain independence?",
        "options": ["A. 1955, B. 1963, C. 1970, D. 1969"],
        "answer": "B"
    },
    {
        "question": "Where is the Maasai Mara located'?",
        "options": ["A. Rift Valley, B. Coast Province, C. Nyanza, D. Eastern Province"],
        "answer": "A"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "What is the name of the famous mobile money service that started in Kenya?",
        "options": ["A. PayPal, B. M-Pesa, C. Airtel Money, D. Orange Cash"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0

    # Shuffle the question order
    random.shuffle(questions)

    print("\n Welcome to SmartBee Game! \n")

    # Loop through questions
    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)

        # Handle invalid inputs
        while True:
            try:
                user_answer = input("Your answer (A/B/C/D): ").strip().upper()
                if user_answer not in ["A", "B", "C", "D"]:
                    raise ValueError("Please enter A, B, C, or D only.")
                break
            except ValueError as e:
                print(e)

        # Compare answers
        if user_answer == q["answer"]:
            print("Correct ✅\n")
            score += 1
        else:
            print(f"Wrong. Correct answer: {q['answer']}\n")
        time.sleep(1)

    # Show total score
    print("Quiz Finished!")
    print(f"Your final score: {score}/{len(questions)}")

    # Feedback
    if score == len(questions):
        print("Excellent!")
    elif score >= len(questions) // 2:
        print("Good job!")
    else:
        print("Try again!")

if __name__ == "__main__":
    run_quiz()
