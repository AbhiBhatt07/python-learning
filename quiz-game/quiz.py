# question and answers in dictionary
quiz = {
    "What is the capital of India? ": "Delhi",
    "Which language is used for web apps? ": "Python",
    "What is the result of 3 + 4? ": "7",
    "Who is the current PM of India? ": "Narendra Modi"
}

score = 0

for question, correct_answer in quiz.items():
    # print(question)
    # print(correct_answer)
    # print(quiz.items())
    user_answer = input(question)

    if user_answer.strip().lower() == correct_answer.lower(): 
        print("✅ Correct!\n")
        score += 1
    
    else:
        print(f"❌ Wrong! The correct answer is: {correct_answer}\n")

print(f"Your total score is: {score}/{len(quiz)} correct!")