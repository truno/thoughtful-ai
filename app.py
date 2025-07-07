from dotenv import load_dotenv
import json
import os
import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage
from langchain.chat_models import init_chat_model

from chatbot import QATool  # Import QATool from chatbot.py

load_dotenv()

st.title("Thoughtful AI Chatbot")
st.markdown("A simple customer service AI agent")

# Check if the API key is available as an environment variable
if not os.getenv('GOOGLE_API_KEY'):
    st.sidebar.header("GOOGLE_API_KEY Setup")
    api_key = st.sidebar.text_input(label="API Key", type="password", label_visibility="collapsed")
    os.environ["GOOGLE_API_KEY"] = api_key
    if not api_key:
        st.info("Please enter your GOOGLE_API_KEY in the sidebar.")
        st.stop()

# Load prepared questions and initialize QATool and LLM
if "qa_tool" not in st.session_state:
    questions = json.load(open("prepared_questions.json", "r"))['questions']
    st.session_state.qa_tool = QATool(prepared_questions=questions)
    st.session_state.llm = init_chat_model("google_genai:gemini-2.0-flash")

if "messages" not in st.session_state:
    st.session_state["messages"] = [AIMessage(content="How can I help you?")]

# Render chat history
for msg in st.session_state.messages:
    if type(msg) == AIMessage:
        st.chat_message("assistant").write(msg.content)
    if type(msg) == HumanMessage:
        st.chat_message("user").write(msg.content)

# Handle new user input
if prompt := st.chat_input():
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        # Use QATool to get the answer
        answer = st.session_state.qa_tool.invoke(prompt, llm=st.session_state.llm)
        st.session_state.messages.append(AIMessage(content=answer))
        msg_placeholder.write(answer)