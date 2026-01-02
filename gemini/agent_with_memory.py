import google.generativeai as genai 
from dotenv import load_dotenv
import os 
from memory_manager import save_to_memory, get_recent_memory

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def ai_agent_with_memory(user_input):
    #load recent memory
    past_memory = get_recent_memory()
    
    history = "\n".join([f"User: {item['user']}\nAgent: {item['agent']}" for item in past_memory])
    
    final_prompt = f"Consider the following conversation history:\n{history}\nNow, respond to the latest user input: {user_input}"
    
    response = model.generate_content(final_prompt)
    agent_response = response.text
    
    save_to_memory({"user": user_input, "agent": agent_response})
    
    return agent_response