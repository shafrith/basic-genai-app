import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 1. Load environment variables
load_dotenv()

# 2. Set up the Streamlit page UI
st.set_page_config(page_title="My AI Assistant", page_icon="🤖")
st.title("🤖 Chat with my AI")

# 3. Initialize the model
llm = ChatOpenAI(model="gpt-4o-mini")

# 4. Initialize Session State for Memory
# st.session_state keeps our memory safe between page re-runs
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful, witty assistant who loves fun facts.")
    ]

# 5. Draw the previous messages on the screen
for message in st.session_state.chat_history:
    # We don't want to display the hidden System instructions to the user
    if isinstance(message, SystemMessage):
        continue
    
    # Pick the right avatar based on who is talking
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    
    with st.chat_message(role):
        st.markdown(message.content)

# 6. The Chat Input Box
# This waits for the user to type and hit Enter
if user_input := st.chat_input("Type your message here..."):
    
    # Display the user's message immediately
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Add the human message to memory
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # 7. Display the AI's response with a streaming effect
    with st.chat_message("assistant"):
        # We extract the text from the LangChain chunks and Streamlit handles the typewriter effect
        stream_generator = (chunk.content for chunk in llm.stream(st.session_state.chat_history))
        full_response = st.write_stream(stream_generator)
        
    # Add the AI's completed response to memory
    st.session_state.chat_history.append(AIMessage(content=full_response))