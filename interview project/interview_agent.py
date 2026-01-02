import google.generativeai as genai
from dotenv import load_dotenv
import os
from memory_manager import save_interview_record, save_strength, save_weakness, get_memory_summmary
from tools import (keyword_match_score, generate_score, improvement_tips,
                   classify_strength_of_weakness, short_feedback)
from roles import chose_role

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model= genai.GenerativeModel('gemini-2.5-flash')


# Function to generate interview question

def generate_question(role):
    prompt = f"""You are an expert interviewer. Generate a challenging interview question for the role of {role.replace("_", " ").title()}. The question should test relevant skills and knowledge for this position. Provide only the question without any additional context or explanation. """
    response = model.generate_content(prompt)
    return response.text.strip()

def analyze_answer(role, role_info, user_answer, difficulty):
    keywords = role_info["keywords"]

    keyword_score = keyword_match_score(user_answer, keywords)
    final_score = generate_score(keyword_score, difficulty)
    tips = improvement_tips(keywords, user_answer)
    brief = short_feedback(role, final_score)
    analysis_prompt = f"""You are an expert interviewer. Provide a detailed analysis of the following answer for the role of {role.replace("_", " ").title()}. The answer is: "{user_answer} 
    1. a short analysis
    2. one sentence on how a recruiter will percive this answer
    3. a one sentence summary of the overall performance.
    """
    
    ai_feedback = model.generate_content(analysis_prompt).text.strip()

    category = classify_strength_of_weakness(final_score)
    if category == "strength":
        save_strength(f"{role.replace('_', ' ').title()}: {ai_feedback}")
    else:
        save_weakness(f"{role.replace('_', ' ').title()}: {ai_feedback}")



    return {
        "final_score": final_score,
        "tips": tips,
        "brief": brief,
        "ai_feedback": ai_feedback
    }


