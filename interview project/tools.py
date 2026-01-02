def keyword_match_score(answer,keywords):
    '''scores teh iuser answer based on the keywor dpresence 
    more keywords  higher score'''
    answer = answer.lower()
    matched = sum(1 for k in keywords if k.lower()  in answer)
    return matched 

def generate_score(keyword_score,difficulty= 'medium'):
    '''generate a final score based on keyword score and difficulty level'''
    
    base = keyword_score * 2

    if difficulty == 'hard':
        base -= 1 

    elif difficulty == 'easy':
        base += 1

    return max(1, min(10, base))  #score between 0 and 10

def improvement_tips(keywords, answer):
    """ returns which important keywords the user missed"""

    answer = answer.lower()
    missed = [k for k in keywords if k.lower() not in answer]
    
    if not missed:
        return "Great job! You covered all the important topics."
    
    missing_list = ",".join(missed)
    return f"You might want to review the following topics: {missing_list}."

def classify_strength_of_weakness(score):
    '''classify the score into strength or weakness'''
    if score >= 7:
        return "strength"
    else:
        return "weakness"
    
def short_feedback(role, score):
    '''provide short feedback based on role and score'''
    if score >= 8:
        return f"Excellent performance in the {role.replace('_', ' ').title()} role!"
    elif score >= 5:
        return f"Good effort in the {role.replace('_', ' ').title()} role, but there's room for improvement."
    else:
        return f"Needs significant improvement in the {role.replace('_', ' ').title()} role."
    
