# ─── Minimal Groq Chatbot ─── #
import streamlit as st
from groq import Groq

# Load in app.py for local dev
#from dotenv import load_dotenv
#import os
#load_dotenv()

#client = Groq(
#    api_key=os.getenv("GROQ_API_KEY")
#)

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Page config
st.set_page_config(page_title="Groq Chatbot", page_icon="⚡")
st.title("⚡ Groq Chatbot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    # Save assistant reply to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })