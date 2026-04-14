# 🤖 IAT Networks AI Chatbot

🚀 **Access the live chatbot here:**  
👉 https://ai-customer-chatbot.streamlit.app/

This project is a Retrieval-Augmented Generation (RAG) based AI chatbot built using data from the IAT Networks website.

The chatbot answers queries related to services, company information, and contact details in a conversational and intelligent manner.

---

## 🚀 Features

- RAG-based retrieval using FAISS
- Conversational memory (last 5 turns)
- Fast responses using Groq LLM (LLaMA 3.1)
- Hybrid system:
  - Structured responses (contact info)
  - Semantic search (services, company details)
- Streamlit UI for real-time interaction
- Assistant persona: Ira

---

## 🏗️ Tech Stack

- Python
- LangChain
- FAISS
- Groq (LLaMA 3.1)
- Sentence Transformers
- Streamlit

---

## 📂 Project Structure

```
ai-customer-support-chatbot/
│
├── app.py
├── chatbot.py
├── data_loader.py
├── vector_store.py
├── memory.py
├── requirements.txt
├── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone repo

```
git clone git@github.com:Muskan2320/ai-customer-support-chatbot.git
cd ai-customer-support-chatbot
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the app

```
streamlit run app.py
```

---

## 🧠 How it works

1. Website data is structured into JSON
2. Converted into semantic chunks
3. Stored in FAISS vector database
4. Query → relevant chunks retrieved
5. LLM generates response
6. Memory keeps last 5 interactions

---

## 🎯 Use Cases

- Customer support chatbot
- Company information assistant
- Service explanation bot

---