from agent import Agent


def main():
    agent = Agent()

    print("🤖 Local Agentic Chatbot")
    print("Model: qwen2.5:latest")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            answer = agent.chat(user_input)
            print(f"AI: {answer}\n")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
