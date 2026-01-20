from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

def init_vector_store():
    return Chroma(
    collection_name="qa_collection",
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory="./data/chroma_langchain_db"
)

def query(question:str, vector_store, top_k:int=4):
    results = vector_store.similarity_search_with_score(
        query=question,
        k=top_k
    )

    print("\n--- Query Results ---")
    print("Question:", question)

    for doc, score in results:
        print("\nChunk Content:", doc.page_content[:300], "...")
        print("Metadata:", doc.metadata)
        print("Score:", score)
    
    return results