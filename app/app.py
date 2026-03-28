import os
import streamlit as st
from openai import OpenAI
import redis
import json

# Env variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VALKEY_HOST = os.getenv("VALKEY_HOST", "valkey")
VALKEY_PORT = int(os.getenv("VALKEY_PORT", 6379))

# OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Valkey (Redis-compatible)
r = redis.Redis(host=VALKEY_HOST, port=VALKEY_PORT, decode_responses=True)

st.title("Simple Chatbot (Docker + Valkey)")

session_id = "chat_session"

# Load history
if r.exists(session_id):
    chat_history = json.loads(r.get(session_id))
else:
    chat_history = []

# Display history
for msg in chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    bot_reply = response.choices[0].message.content

    chat_history.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save to Valkey
    r.set(session_id, json.dumps(chat_history))