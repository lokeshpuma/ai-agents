import google.generativeai as genai
from dotenv import load_dotenv
import os
from api_tools import get_current_time

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def router_agent(query):
    if "time " in query.lower():
        return f"the current time is :{get_current_time()}"
    
    if "explain" in query.lower() or "explanation" in query.lower():
        return model.generate_content(f"Provide a detailed explanation for the following query:\n{query}").text

    #default fallback

    return model.generate_content(query).text


if __name__ == "__main__":
    user_query = "Can you explain quantum computing in simple terms?"
    print(router_agent(user_query))
    print(router_agent("what is the current time in Kolkata?"))
