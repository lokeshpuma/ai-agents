from interview_agent import generate_question, analyze_answer
from memory_manager import save_interview_record, get_memory_summmary

class InterviewRouter:
    def __init__(self,role,role_data):
        self.role = role
        self.role_data = role_data
        self.question_count = 0
        self.max_questions = 3
        self.waiting_for_answer = False
        self.current_question = ""

    def next_step(self,user_input= None):
        if self.question_count==0:
            return self._ask_new_question()
        
        if self.waiting_for_answer and user_input:
            return self._process_answer(user_input)
        
        if self.question_count < self.max_questions:
            return self._ask_new_question()
        
        return self._final_report()
    
    def _ask_new_question(self):
        self.current_question = generate_question(self.role)
        self.question_count += 1
        self.waiting_for_answer = True
        return {
            "type": "question",
            "content": self.current_question
        }
    
    def _process_answer(self,user_answer):
        self.waiting_for_answer = False

        feedback = analyze_answer(self.role, self.role_data, user_answer, self.role_data["difficulty_levels"][0])
        save_interview_record(self.role, self.current_question, user_answer, feedback)

        return {
            "type": "feedback",
            "content": feedback["final_score"],
            "brief": feedback["brief"],
            "improvement": feedback["tips"],
            "ai_feedback": feedback["ai_feedback"]
        
        }
    def _final_report(self):
        summary = get_memory_summmary()
        return {
            "type": "final_report",
            "total_questions": self.question_count,
            "strengths": summary["strengths"][-5:],
            "weaknesses": summary["weaknesses"][-5:],
            "message": "Interview session completed. Here is your summary."
        }
    

