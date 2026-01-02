import google.generativeai as genai
from dotenv import load_dotenv
import os
import concurrent.futures

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompts = [
        "Explain the theory of relativity in simple terms.",
        "What is the capital of France?",
        "How does photosynthesis work?",
        "Tell me a joke about computers.",
        "What are the benefits of meditation?"
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(ask_gemini, prompt): prompt for prompt in prompts}
        for future in concurrent.futures.as_completed(futures):
            prompt = futures[future]
            try:
                answer = future.result()
                print(f"Prompt: {prompt}\nAnswer: {answer}\n")
            except Exception as e:
                print(f"Prompt: {prompt}\nError: {str(e)}\n")
