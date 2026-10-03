import streamlit as st

from agent import Agent


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Agentic AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Initialize Agent
# -----------------------------

if "agent" not in st.session_state:
    st.session_state.agent = Agent()


# -----------------------------
# Header
# -----------------------------

st.title(" Agentic AI Chatbot")
st.caption("Powered by Qwen 2.5 + Ollama")


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("Settings")

    st.write("**Model:**")
    st.code("qwen2.5:latest")

    st.divider()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.agent = Agent()
        st.rerun()


# -----------------------------
# Display chat history
# -----------------------------

for message in st.session_state.agent.memory.get_messages():

    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])

    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])


# -----------------------------
# Chat input
# -----------------------------

user_input = st.chat_input("Ask me anything...")


if user_input:

    # Display user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            try:
                response = st.session_state.agent.chat(user_input)

                st.write(response)

            except Exception as e:
                st.error(f"Something went wrong: {e}")