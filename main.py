import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI
import chromadb

from pydantic import BaseModel

class QuestionData(BaseModel):
    question: str

app = FastAPI()
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# Create ChromaDB client
client = chromadb.Client()

# Create/Get Collection
collection = client.get_or_create_collection(
    name="ai_notes"
)


# Fixed Size Chunking Function
def create_chunks(text, chunk_size=100):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


@app.post("/ask")
def ask_question(user_question: QuestionData):

    # Read Notes File
    with open("ai_notes.txt", "r") as file:

        content = file.read()

    # Create Chunks
    chunks = create_chunks(content)

    # Print Chunks
    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i+1}")
        print(chunk)
        print("-" * 50)

    # Store Chunks in ChromaDB
    try:

        collection.add(
            documents=chunks,
            ids=[f"chunk_{i}" for i in range(len(chunks))]
        )

    except Exception:
        pass

    # Query ChromaDB
    results = collection.query(
        query_texts=[user_question.question],
        n_results=1
    )
    retrieved_chunk = results["documents"][0][0]

    print("\nRetrieved Chunk:")
    print(retrieved_chunk)

    # STEP 4: Create Prompt
    prompt = f"""
    Context:
    {retrieved_chunk}

    Question:
    {user_question.question}

    Explain it in simple words.
    """

# STEP 5: Send to Gemini
    response = model.generate_content(
    prompt
    )

# STEP 6: Return Answer
    return {
    "retrieved_chunk": retrieved_chunk,
    "answer": response.text
}

    print("\nRetrieved Result:")
    print(results)

    print("\nTotal Chunks Stored:")
    print(collection.count())

    return {
        "chunks": chunks,
        "retrieved": results["documents"][0]
    }

   