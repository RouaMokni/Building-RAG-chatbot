import json
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

# Embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load JSON file
file_path = "./data/data.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

documents = []

for item in data["questions"]:
    question = item["question"]
    answer = item["answer"]

    content = f"Question: {question}\nAnswer: {answer}"

    documents.append(
        Document(
            page_content=content,
            metadata={
                "source": "json_file",
                "filename": "data.json",
                "question": question
            }
        )
    )

# Generate UUIDs
uuids = [str(uuid4()) for _ in documents]

# Create / load vector store
vector_store = Chroma(
    collection_name="qa_collection",
    embedding_function=embeddings,
    persist_directory="./data/chroma_langchain_db"
)

# Add documents
vector_store.add_documents(documents=documents, ids=uuids)
