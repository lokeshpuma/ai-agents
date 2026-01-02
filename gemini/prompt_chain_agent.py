import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def chain(prompt):
    # step 1 : ask agent to break down the task
    step_1 = model.generate_content(f"Break down the following task into 3 sub-tasks:\n{prompt}").text

    print("\n Step 1 - Breakdown:\n",step_1)

    # step 2 : ask agent to complete the reasoning

    step_2 = model.generate_content(f"Based on the following breakdown, provide detailed reasoning for each sub-task:\n{step_1}").text
    print("\n [Explanation]:\n",step_2)

    # step 3 : ask agent to provide final response

    step_3 = model.generate_content(f"summarize the answers in simple steps").text

    print("\n [Summary]:\n",step_3)

    return step_3


if __name__ == "__main__":
    user_prompt = "Explain the theory of relativity in simple terms and provide an example of its application in everyday life."
    chain(user_prompt)