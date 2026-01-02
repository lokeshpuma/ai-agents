from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
response = openai.ChatCompletion.create(
    engine = "text-davinci-003",
    prompt = "Hello, how are you?",
    max_tokens = 5
)
print(response.choices[0].text.strip())