import ollama

from memory import ConversationMemory


class Agent:
    def __init__(self):
        self.memory = ConversationMemory()
        self.model = "qwen2.5:latest"

    def chat(self, user_message):
        self.memory.add_user_message(user_message)

        response = ollama.chat(
            model=self.model,
            messages=self.memory.get_messages()
        )

        answer = response["message"]["content"]

        self.memory.add_assistant_message(answer)

        return answer
