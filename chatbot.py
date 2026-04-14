import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from data_loader import load_documents
from vector_store import create_or_load_vectorstore
from memory import get_memory
from functools import lru_cache
import streamlit as st

# ----------------------------
# Load environment variables
# ----------------------------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    groq_api_key = st.secrets["GROQ_API_KEY"]

# ----------------------------
# Memory (last 5 turns)
# ----------------------------
memory = get_memory()

# ----------------------------
# LLM (Groq)
# ----------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=groq_api_key
)

# ----------------------------
# Prompt
# ----------------------------
prompt_template = """
You are Ira, a professional AI assistant for IAT Networks.

Guidelines:
1. Answer clearly, confidently, and professionally.
2. Use ONLY the provided context.
3. Do NOT mention phrases like "based on context" or "unfortunately".
4. If information is partially available, provide the best complete answer using available details.
5. If no relevant information exists, respond politely:
   "I don’t have that information. Please contact our team."

Keep responses concise and helpful.

Context:
{context}

Chat History:
{chat_history}

Question:
{question}

Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "chat_history", "question"]
)

# ----------------------------
# Load system once (cached)
# ----------------------------
@lru_cache(maxsize=1)
def load_system():
    documents, raw_data = load_documents()
    vectorstore = create_or_load_vectorstore(documents)
    return vectorstore, raw_data

vectorstore, raw_data = load_system()

# ----------------------------
# RAG Chain
# ----------------------------
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": PROMPT}
)

# ----------------------------
# Router + fallback
# ----------------------------
def handle_query(query):
    q = query.lower()

    if q.strip() in ["hi", "hello", "hey"]:
        return "Hello! I’m Ira. How can I assist you today?"

    if any(word in q for word in ["thank", "thanks", "thank you"]):
        return "You're welcome! Let me know if you need anything else."

    if any(word in q for word in ["bye", "goodbye"]):
        return "Goodbye! Feel free to reach out anytime."

    # Structured response
    if any(word in q for word in ["contact", "phone", "email", "address"]):
        return (
            f"Phone: {raw_data['contact']['phone']}\n"
            f"Email: {raw_data['contact']['email']}\n"
            f"Address: {raw_data['contact']['address']}"
        )

    # RAG response
    result = qa_chain.invoke({"question": query})
    response = result["answer"]

    # Fallback
    if not response or "i don’t have that information" in response.lower():
        return (
            "I don’t have that information. "
            f"Please contact us at {raw_data['contact']['email']} "
            f"or call {raw_data['contact']['phone']}."
        )

    return response