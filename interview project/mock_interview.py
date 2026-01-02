from roles import chose_role
from router import InterviewRouter

def run_interview():
    print("\n Welcome to the Mock Interview Platform!\n")

    role ,role_data = chose_role()
    router = InterviewRouter(role, role_data)

    print("\nStarting the interview session...\n")

    while True:
        step = router.next_step()

        if step["type"] == "question":
            print(f"Question {router.question_count}: {step['content']}\n")
            user_answer = input("Your Answer: ")
            step = router.next_step(user_answer)

        if step["type"] == "feedback":
            print(f"\nFeedback:\nScore: {step['content']}\nBrief: {step['brief']}\nImprovement Tips: {step['improvement']}\nAI Feedback: {step['ai_feedback']}\n")

        if step["type"] == "final_report":
            print("\nFinal Report:")
            print(f"Total Questions Asked: {step['total_questions']}")
            print("Strengths:")
            for strength in step["strengths"]:
                print(f"- {strength}")
            print("Weaknesses:")
            for weakness in step["weaknesses"]:
                print(f"- {weakness}")
            print(step["message"])
            break


if __name__ == "__main__":
    run_interview()