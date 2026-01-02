import json
import os

MEMORY_FILE = 'interview_memory.json'

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'w') as f:
        json.dump({"history":[],"strengths":[],"weaknesses":[]}, f)

def save_interview_record(role,question,user_answer,feedback):
    """save one interview record to memory file"""
    try:
        with open(MEMORY_FILE, 'r') as f:
            memory = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        memory = {"history":[],"strengths":[],"weaknesses":[]}

    record = {
        "role": role,
        "question": question,
        "user_answer": user_answer,
        "feedback": feedback
    }

    memory["history"].append(record)
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=4)

def save_strength(strength):
    """save a strength to memory file"""
    try:
        with open(MEMORY_FILE, 'r') as f:
            memory = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        memory = {"history":[],"strengths":[],"weaknesses":[]}

    memory["strengths"].append(strength)
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=4)

def save_weakness(weakness):
    """save a weakness to memory file"""
    try:
        with open(MEMORY_FILE, 'r') as f:
            memory = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        memory = {"history":[],"strengths":[],"weaknesses":[]}

    memory["weaknesses"].append(weakness)
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=4)

def get_memory_summmary():
    """retrieve a summary of the interview memory"""
    try:
        with open(MEMORY_FILE, 'r') as f:
            memory = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        memory = {"history":[],"strengths":[],"weaknesses":[]}

    return memory