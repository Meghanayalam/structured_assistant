# 🤖 Structured Assistant – Build Your First AI Task Agent

Welcome to **Structured Assistant** — a minimal yet powerful backend application that simulates the early design of an AI assistant. It stores memory, handles requests, and paves the way to build intelligent, stateful agents. If you're starting your journey in AI/ML backend systems or just love tinkering with modern Python frameworks, you're in the right place.

---

## ✨ Why This Project Matters

With the boom in LLMs, voice assistants, and agent-based AI systems, **learning to build modular, memory-aware assistant frameworks is invaluable**. This project demonstrates:

- 🧠 How to store and manage conversational memory
- 🧩 How to modularize backend logic
- 🚀 How to use FastAPI to build robust, scalable APIs
- ⚡ How to structure projects like a production-grade backend

It’s simple enough for beginners, but extensible enough to impress on your resume or GitHub profile.



## 🧠 What It Does (At a Glance)

1. Accepts user messages via an API (`/chat`)
2. Loads previous conversations from a local `memory.json`
3. Passes the message to a task handler (`task_agent.py`)
4. Responds with a structured answer (or a fallback if not supported)
5. Saves the new conversation back into memory

All in real-time. All through FastAPI.



## 📦 Project Architecture

structured_assistant/
├── app.py # FastAPI app with /chat endpoint
├── memory.py # Functions to load and save chat history
├── task_agent.py # Handles and responds to tasks
├── requirements.txt # Python dependencies
├── data/
│ └── memory.json # Stores conversation memory (JSON list)
└── venv/ # Virtual environment (ignored)


This is designed for clarity. Each component has **one responsibility**.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Meghanayalam/structured_assistant.git
cd structured_assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
uvicorn app:app --reload
curl -X POST http://127.0.0.1:8000/chat \
-H "Content-Type: application/json" \
-d '{"message": "Hello, assistant!"}'
{
  "response": "I'm not sure how to respond to that yet."
}

Customize the logic in task_agent.py to give smarter responses!





















