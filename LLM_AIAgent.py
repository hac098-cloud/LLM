from openai import OpenAI

client = OpenAI()

def calculator_tool(user_input):
    try:
        expression = user_input.lower().replace("calculate", "").strip()
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Sorry, I cannot calculate that."

def study_plan_tool(topic):
    topic = topic.replace("study plan", "").strip()
    if not topic:
        topic = "programming"

    return (
        "Study plan for {topic}:\n"
        "Day 1: Learn the basics\n"
        "Day 2: Practice with examples\n"
        "Day 3: Build a small project"
    )

def joke_tool():
    return "Here is a joke."

def ask_llm(user_input):
    response = client.responses.create(
        model="gpt-5.5",
        instructions="You are a beginner-friendly AI assistant. Explain simply.",
        input=user_input
    )
    return response.output_text

def agent(user_input):
    lower = user_input.lower()

    if "calculate" in lower:
        return calculator_tool(user_input)

    elif "study plan" in lower:
        return study_plan_tool(user_input)

    elif "joke" in lower:
        return joke_tool()

    else:
        return ask_llm(user_input)

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    print("Agent:", agent(user))