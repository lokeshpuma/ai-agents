from agent_with_memory import ai_agent_with_memory

print("AI agent with memory (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    agent_response = ai_agent_with_memory(user_input)
    print("Agent:", agent_response)

print("Goodbye!")