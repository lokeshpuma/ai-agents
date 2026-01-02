from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    exit(1)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_response(prompt):
    try: 
        response = model.generate_content(prompt)
        print("\n Response:\n",response.text)
    except Exception as e:
        print("An error occurred while generating the response:", str(e))

if __name__ == "__main__":
    generate_response("Tell me a funny AI joke in one sentence")



