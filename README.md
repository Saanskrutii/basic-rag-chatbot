# Basic RAG Chatbot

A beginner-friendly Retrieval Augmented Generation (RAG) chatbot built using FastAPI, Gemini, and ChromaDB.

## 🚀 Features

- FastAPI Backend
- Gemini LLM Integration
- ChromaDB Vector Database
- Fixed Size Chunking
- Semantic Search
- Retrieval Augmented Generation (RAG)

---

## 🛠 Tech Stack

- Python
- FastAPI
- Google Gemini API
- ChromaDB
- Sentence Transformers
- Pydantic

---

## 📖 How It Works

### 1. Read Document

The application reads data from:

```text
ai_notes.txt
```

### 2. Chunking

The document is split into smaller chunks using fixed-size chunking.

```text
Document
 ↓
Chunk 1
Chunk 2
Chunk 3
```

### 3. Store in ChromaDB

ChromaDB converts chunks into embeddings and stores them as vectors.

```text
Chunk
 ↓
Embedding
 ↓
Vector
 ↓
ChromaDB
```

### 4. User Question

The user submits a question through the API.

```text
"What is RAG?"
```

### 5. Retrieval

ChromaDB:

- Converts the question into an embedding
- Compares it with stored vectors
- Retrieves the most relevant chunk

```text
Question
 ↓
Embedding
 ↓
Vector Similarity Search
 ↓
Relevant Chunk
```

### 6. Generation

The retrieved chunk is sent to Gemini along with the user's question.

```text
Retrieved Context
 +
User Question
 ↓
Gemini
 ↓
Final Answer
```

---

## 🔄 RAG Pipeline

```text
User Question
      ↓
FastAPI
      ↓
Chunking
      ↓
ChromaDB
      ↓
Retrieve Relevant Chunk
      ↓
Gemini
      ↓
Generated Answer
```

---

## 📂 Project Structure

```text
basic-rag-chatbot/

│
├── main.py
├── ai_notes.txt
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── test_chroma.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd basic-rag-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

---

## ▶️ Run Application

```bash
python -m uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 📌 Sample Request

```json
{
  "question": "What is RAG?"
}
```

### Sample Response

```json
{
  "retrieved_chunk": "RAG stands for Retrieval Augmented Generation.",
  "answer": "RAG is a technique that retrieves relevant information before generating an answer."
}
```

---

## 🎯 Learning Outcomes

Through this project I learned:

- FastAPI API Development
- Gemini API Integration
- Embeddings
- Vector Databases
- ChromaDB
- Chunking
- Semantic Search
- Retrieval Augmented Generation (RAG)

---

## 🏆 Project Status

✅ FastAPI Working

✅ ChromaDB Working

✅ Retrieval Working

✅ Gemini Integration Working

✅ Dynamic User Questions

✅ Basic RAG Pipeline Completed

---

## 👩‍💻 Author

**Sanskruti Gosavi**
