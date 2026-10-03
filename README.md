🤖 Agentic AI Chatbot

A beginner-friendly Agentic AI chatbot built with Python, Ollama, Qwen 2.5, and Streamlit.

This is my first basic Agentic AI project. The goal of this project is to understand the fundamental concepts behind AI agents, including LLM interaction, conversation memory, tools, and a user interface.

The chatbot runs locally using Qwen 2.5 through Ollama, so the AI model does not need to be hosted on a cloud API for the basic chatbot functionality.

🚀 Project Overview

This project demonstrates how to build a simple AI chatbot from scratch and gradually move toward an agentic architecture.

The application currently contains:

 Chat interface using Streamlit

 Conversation memory

 Local Qwen 2.5 LLM

 Ollama for running the model locally

 Basic tools such as calculator and date/time utilities

 Python backend

 Streamlit frontend

The project is intentionally kept simple because it is designed as a learning project.


Technologies Used

Python

Python is used as the main programming language for the project.

Ollama

Ollama allows the project to run an LLM locally on the computer.

The model used in this project is:

qwen2.5:latest

Qwen 2.5

Qwen 2.5 is the local language model responsible for generating chatbot responses.

Streamlit

Streamlit is used to create the web interface for the chatbot without needing to build a separate frontend using HTML, CSS, and JavaScript.

 What Is Agentic AI?

A traditional chatbot generally follows this pattern:

User
  ↓
LLM
  ↓
Response


An AI agent can go further by using tools, memory, and decision-making logic:

User
  ↓
Agent
  ↓
Decide what to do
  ↓
Use a tool if necessary
  ↓
Get result
  ↓
LLM
  ↓
Final response


This project is a basic introduction to this architecture.

The project will gradually evolve from a simple chatbot into a more capable AI agent.

 Current Tools

The project includes basic tools such as:

Calculator

The calculator can evaluate mathematical expressions.

Example:

25 * 4


Result:

100

Current Date

The agent can retrieve the current date.

Current Time

The agent can retrieve the current local time.

 Conversation Memory

The project contains a simple conversation memory system.

For example:

User: My name is Alex.

AI: Nice to meet you, Alex.

User: What is my name?

AI: Your name is Alex.


The previous messages are stored and sent along with new messages so the model has conversational context.

The memory implementation is located in:

memory.py

💻 Installation
1. Clone or download the project

Open the project directory:

cd "C:\Users\YourName\Desktop\agentic chatbot"

2. Create a virtual environment

It is recommended to use a virtual environment:

python -m venv .venv


Activate it on Windows:

.venv\Scripts\activate


You should then see something similar to:

(.venv) PS C:\Users\YourName\Desktop\agentic chatbot>

3. Install dependencies
python -m pip install -r requirements.txt


If Streamlit is not installed:

python -m pip install streamlit

 Ollama Setup

Install Ollama on your computer and make sure it is running.

Check the installed models:

ollama list


This project uses:

qwen2.5:latest


You can test the model with:

ollama run qwen2.5:latest


If Qwen responds, your local model is working correctly.

 Running the Application

Start the Streamlit application with:

python -m streamlit run streamlit_app.py


Streamlit will provide a local URL similar to:

http://localhost:8501


Open that URL in your browser.

💬 Example

After starting the application, you can ask:

Hello!

What is artificial intelligence?

Explain what an AI agent is.

Calculate 125 * 25

What is today's date?

🔐 Environment Variables

The .env file can be used for configuration.

For example:

OLLAMA_MODEL=qwen2.5:latest


Do not commit sensitive API keys or secrets to GitHub.

A .gitignore file should contain:

.env
.venv/
__pycache__/
*.pyc

🎯 Learning Goals

This project is primarily a learning project.

The main concepts I am learning are:

Understanding how LLMs work with applications

Calling a local LLM from Python

Understanding AI agents

Building conversation memory

Creating tools for an AI agent

Connecting tools with an LLM

Building a chatbot UI with Streamlit

Understanding the difference between a chatbot and an agent

Building an AI application step by step

🗺️ Future Improvements

This is the first/basic version of the project.

Possible future improvements include:

🔧 Proper LLM tool calling

🌐 Web search tool

📄 Document Q&A

📚 RAG (Retrieval-Augmented Generation)

🧠 Long-term memory

🗂️ Conversation history

🔐 Better configuration management

⚡ Streaming responses

🎨 Improved Streamlit UI

🤝 Multiple specialized agents

📊 Agent/tool execution logs

🧪 Automated tests

📚 Agentic AI Learning Path

The project can evolve through the following stages:

Stage 1
Basic LLM Chatbot
        ↓
Stage 2
Conversation Memory
        ↓
Stage 3
Tools
        ↓
Stage 4
Tool Calling
        ↓
Stage 5
Agent Decision Making
        ↓
Stage 6
RAG
        ↓
Stage 7
Long-Term Memory
        ↓
Stage 8
Multi-Agent Systems


The goal is to understand each stage before moving to the next one.

Project Status

Status: Beginner / Learning Project

Type: Agentic AI / LLM Application

Model: Qwen 2.5

Model Runtime: Ollama

Frontend: Streamlit

Language: Python

 About

This project was created as my first Agentic AI project to learn the fundamentals of building AI-powered applications.

The project focuses on understanding the concepts and architecture behind AI agents rather than relying entirely on high-level frameworks.

📄 License

This project is intended for learning and experimentation.