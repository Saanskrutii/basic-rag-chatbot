# test_chroma.py

import chromadb

client = chromadb.Client()

collection = client.create_collection("test")

print("ChromaDB Working!")