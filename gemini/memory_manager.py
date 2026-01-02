import json
import os
MEMORY_FILE = "agent_memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"history": []}, f)

def save_to_memory(entry):
    """Saves an entry to the agent's memory file."""
    with open(MEMORY_FILE,"r") as f:
        data = json.load(f)

    data["history"].append(entry)

    with open(MEMORY_FILE,"w") as f:
        json.dump(data,f,indent=4)

def get_recent_memory (n=5):
    """retrieves the last n entries from the agent's memory."""
    with open(MEMORY_FILE,"r") as f:
        data = json.load(f)
    return data["history"][-n:]
