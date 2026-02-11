import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load local .env
load_dotenv()

st.header("AI Chat App")

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("HF_TOKEN not found in environment variables.")
    st.stop()

# Create HF Router client (OpenAI compatible)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

prompt = st.text_input("Enter a prompt")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            completion = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3.2:novita",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200
            )

        result = completion.choices[0].message.content

        st.write(result)

        st.session_state.chat_history.append(("User", prompt))
        st.session_state.chat_history.append(("AI", result))
    else:
        st.warning("Please enter some text")

st.header("Chat History")

for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")
