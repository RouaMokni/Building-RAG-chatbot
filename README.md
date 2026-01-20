# 🤖 Chatbot with Vector Store (Initial Implementation)

This project is an initial implementation of a chatbot that supports data storage and semantic querying using vector embeddings.

## ✨ Features
- Vector store initialization and querying using **Chroma** and **OpenAI embeddings**
- API endpoints for:
  - Querying stored data
  - Chatting with the chatbot
- Included sample data files for questions and answers

## 🚀 How to Run the Project

```bash
# 1️⃣ Create a virtual environment
python -m venv venv

# 2️⃣ Activate the virtual environment
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure environment variables
# Create a .env file and add your configuration:
OPENAI_API_KEY=your_api_key_here

# 5️⃣ Run the FastAPI server
uvicorn main:app --reload

# 6️⃣ Access the API
API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
