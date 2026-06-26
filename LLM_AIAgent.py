import random

from openai import OpenAI

# Create an OpenAI client to connect to the OpenAI API
client = OpenAI()


# Tool 1: Calculator
def calculator_tool(user_input):
    try:
        # Remove the word "calculate" and keep only the math expression
        expression = user_input.lower().replace("calculate", "").strip()

        # Calculate the expression
        result = eval(expression)

        # Return the result
        return f"Result: {result}"

    except Exception:
        # Return an error if the input is invalid
        return "Sorry, I cannot calculate that."


# Tool 2: Study Plan
def study_plan_tool(topic):

    # Remove the keyword "study plan"
    topic = topic.replace("study plan", "").strip()

    # Use a default topic if the user doesn't provide one
    if not topic:
        topic = "programming"

    # Return a simple 3-day study plan
    return (
        f"Study plan for {topic}:\n"
        "Day 1: Learn the basics\n"
        "Day 2: Practice with examples\n"
        "Day 3: Build a small project"
    )


# Tool 3: Joke
def joke_tool():
    # Return a fixed joke
    joke = [
        "Here is a joke.",
        "I am you.",
        "Python is funny."
    ]

    return random.choice(joke) 
    

# Send the user's question to the LLM
def ask_llm(user_input):
  try:
    # Call the OpenAI API
    response = client.responses.create(

        # Choose which LLM to use
        model="gpt-5.5",

        # Give the LLM a system instruction
        instructions="You are a beginner-friendly AI assistant. Explain simply.",

        # Send the user's question
        input=user_input
    )

    # Return the LLM's answer
    return response.output_text
  except Exception:
    return "Sorry, I cannot process that."

# AI Agent
def agent(user_input):

    # Convert input to lowercase for easier matching
    lower = user_input.lower()

    # Decide which tool to use
    if "calculate" in lower:
        return calculator_tool(user_input)

    elif "study plan" in lower:
        return study_plan_tool(user_input)

    elif "joke" in lower:
        return joke_tool()

    # If no tool matches, ask the LLM
    else:
        return ask_llm(user_input)


# Keep chatting until the user types "exit"
while True:

    # Get user input
    user = input("You: ")

    # Exit the program
    if user.lower() == "exit":
        break

    # Print the agent's response
    print("Agent:", agent(user))