import streamlit as st
import google.generativeai as genai
import os
from config import API_KEY  # Assuming API key is stored in config.py

# Initialize Google Generative AI client
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Google Generative AI Chat")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.get("assistant_prompt") is None:
    st.session_state["assistant_prompt"] = "Write a story about a magic backpack."

if prompt := st.text_input("You:", value=st.session_state["assistant_prompt"]):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response using Google Generative AI model
    response = model.generate_content(prompt)
    
    st.session_state["messages"].append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)

# Save session state
st.session_state.sync()
