import streamlit as st
from transformers import pipeline
import torch

st.header("AI Chat App")

Generator = pipeline("text-generation", model="distilgpt2")

if "Chat history" not in st.session_state:
  st.session_state.chat_history = []
  
prompt = st.text_input("Enter a prompt")

if st.button("Generate"):
  if prompt:
    result = Generator(prompt, max_length=50)
    st.write(result)

    st.session_state.chat_history.append(("Users",prompt))
    st.session_state.chat_history.append(("AI",result))

  else:
    st.warning("Please enter some text")

st.header("Chat History")
for role, text in st.session_state.chat_history:
  st.write(f"**{role}:** {text}")



