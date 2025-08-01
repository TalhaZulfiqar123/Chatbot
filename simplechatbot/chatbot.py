import streamlit as st
import os
from groq import Groq

# Streamlit setup
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Simple Groq Chatbot")

# API Key input
groq_api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
model = st.sidebar.selectbox("Choose a model", ["mixtral-8x7b-32768", "llama3-70b-8192", "gemma-7b-it"])

# Save key to env for Groq client
if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key
    client = Groq(api_key=groq_api_key)
else:
    st.warning("Please enter your Groq API key in the sidebar.")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask something:", key="user_input")

# Send message
if st.button("Send") and user_input:
    if not groq_api_key:
        st.error("API key is missing!")
    else:
        try:
            # Call Groq API
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                model=model,
            )

            reply = response.choices[0].message.content
            st.session_state.chat_history.append(("🧑 You", user_input))
            st.session_state.chat_history.append(("🤖 Bot", reply))
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display chat
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
