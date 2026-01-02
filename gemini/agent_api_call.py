import google.generativeai as genai
from dontenv import load_dotenv
import os
from api_tools import get_current_time

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_response(prompt):
    if "time" in prompt.lower():
        real_time = get_current_time()
        prompt += f"\n\nCurrent time in Asia/Kolkata is: {real_time}"

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompt = "what is the current time in Kolkata?"
    print(generate_response(prompt))
