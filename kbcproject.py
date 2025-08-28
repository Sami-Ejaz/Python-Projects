
import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A) 11", "B) 30", "C) 20", "D) 25"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Shakespeare", "B) Dickens", "C) Wordsworth", "D) Keats"],
        "answer": "A"
    },
    # Add more questions as needed
]

random.shuffle(questions)

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    
    user_input = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_input == q["answer"]:
        score += 1
        print("Correct!")
        if score == 20:
            print("\nCongratulations! You answered 20 questions correctly!")
            break
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")
        break

print(f"\nYour final score is: {score}")


# questions=[
#     {
#     "question":"what is capital of pakistan",
#     "options":["a) Islamabad","b) karachi","c) lahore"],
#     "answer":"a"

#     },
#     {
#     "question":"what is capital of kpk",
#     "options":["a) abbottabad","b) peshwar","c) lahore"],
#     "answer":"b"

#     },
#     {
#     "question":"what is capital of punjab",
#     "options":["a) Islamabad","b) karachi","c) lahore"],
#     "answer":"c"

#     },
#     {
#     "question":"what is capital of pakistan team",
#     "options":["a) Salman Agha","b) baber","c) rizwan"],
#     "answer":"a"

#     },
#     {
#     "question":"what is capital of india",
#     "options":["a) Islamabad","b) new Delhi","c) lahore"],
#     "answer":"b"

#     }
#     {
#     "question":"what is 2+2",
#     "options":["a) 5","b) 8","c) 4"],
#     "answer":"c"

#     },
#     {
#     "question":"which one of the following is srk movie ",
#     "options":["a) dhoom","b) joker","c) fan"],
#     "answer":"c"

#     },
#     {
#     "question":"who won last cricket worldcup",
#     "options":["a) india","b) china","c) pakistan"],
#     "answer":"a"

#     },
#     {
#     "question":"name the most advanced jet of pakistan",
#     "options":["a) b2","b) f16","c) jf17 thunder"],
#     "answer":"c"

#     },
# ]
# random.shuffle(questions)
# score=0
# for q in questions:
#     print("\n" + q["question"])
#     for opt in q["options"]:
#         print(opt)
#     user_input = input("Enter your answer (a/b/c): ")

#     if user_input == q["answer"]:
#         score += 1
#         print("Correct!")
#         if score == 20:
#             print("\nCongratulations! You answered 20 questions correctly!")
#             break
#     else:
#         print(f"Wrong! The correct answer was {q['answer']}.")
#         break

# print(f"\nYour final score is: {score}")