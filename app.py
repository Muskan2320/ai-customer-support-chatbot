import streamlit as st
from chatbot import handle_query

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="IAT Chatbot", layout="centered")

st.title("IAT Networks Chatbot")
st.markdown("Ask about services, contact info, or company details")

# ----------------------------
# Initialize chat history
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Default greeting
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello, I am Ira. How can I help you?"
    })

# ----------------------------
# Display chat history
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# User input
# ----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Get bot response
    response = handle_query(user_input)

    # Store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)