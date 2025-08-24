# backend/memory.py
import chromadb
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings

# For simplicity we store locally using chroma default
client = chromadb.Client(Settings())

def upsert_docs(collection_name: str, docs: list[str], metadatas=None):
    coll = client.get_or_create_collection(collection_name)
    # naive: embed externally or leave raw
    for i, d in enumerate(docs):
        coll.add(ids=[f"{collection_name}_{i}"], documents=[d], metadatas=[{}])

def query_similar(collection_name: str, query: str, n=3):
    coll = client.get_collection(collection_name)
    res = coll.query(query_texts=[query], n_results=n)
    return res
