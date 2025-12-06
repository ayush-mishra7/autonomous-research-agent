# 🚀 Autonomous Research Agent (ARA)
### **An Offline, Fast, Multi-Agent Research System Powered by Ollama + FastAPI**

The **Autonomous Research Agent (ARA)** is a lightweight, fully offline AI system designed to generate structured research reports using a modular multi-agent architecture.  
It uses **local LLMs via Ollama**, ensuring:

- Zero API cost  
- Zero rate limits  
- Zero dependency on cloud models  
- Works even without internet  

Perfect for low-resource machines, students, AI beginners, and offline research automation.

---

## 📌 Key Features

- 🔍 **Researcher Agent** — generates structured research notes  
- ✍️ **Writer Agent** — creates polished research reports  
- 🤖 **LLM Client** — interfaces with lightweight local models (Qwen / Phi-3 / Gemma)  
- 🌐 **FastAPI Backend** — fully functional REST API  
- 🔌 **Runs 100% Offline** — no API keys, no credits needed  
- ⚙️ **Low Resource Optimized** — uses <500MB local models  
- 🧩 **Modular Architecture** — easily extendable with more agents  

---

## 🏗️ Architecture Diagram

            ┌────────────────┐
            │    FastAPI     │
            │  /research API │
            └───────▲────────┘
                    │ topic
                    │
            ┌──────────────────┐
            │ Researcher Agent │
            └───────▲──────────┘
                    │ notes
                    │
            ┌──────────────────┐
            │  Writer Agent    │
            └───────▲──────────┘
                    │ final report
                    │
            ┌────────────────┐
            │  LLM Client    │
            │  Ollama Local  │
            └────────────────┘


---

## 📂 Project Structure

autonomous-research-agent/
│
├── main.py
├── requirements.txt
├── Dockerfile
│
└── src/
├── init.py
│
├── agents/
│ ├── init.py
│ ├── llm_client.py
│ ├── researcher_agent.py
│ └── writer_agent.py
│
└── api/
├── init.py
└── server.py

---

## 🔧 Installation

### 1️⃣ Install Ollama  
Download here:  
https://ollama.com/download

### 2️⃣ Pull a lightweight local model  
Recommended (fast):

```bash
ollama pull qwen2.5:0.5b
```

### 3️⃣ Install Python dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Running the FastAPI Server
```bash
uvicorn src.api.server:app --reload
```
### 🧪 Example API Request
POST /research

Request:
```bash
{
  "topic": "Agentic AI"
}
```
Response:
```bash
{
  "topic": "Agentic AI",
  "report": "Executive Summary...\nKey Insights..."
}
```
### 🖥 Running from CLI
```bash
python main.py
```
Input:
```bash
Agentic AI 2.0
```

### 🐳 Docker Support

Build the container:
```bash
docker build -t ara-api .
```
Run:
```bash
docker run -p 8000:8000 ara-api
```
---
## 🧩 Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Ollama
- Qwen2.5 / Phi-3 / Gemma Models
- httpx
- Modular Multi-Agent Architecture

## 🚀 Future Enhancements (Planned)

- Web Scraping Agent
- RAG + Vector Database
- Multi-Agent Collaboration
- PDF Exporter (styled reports)
- React or Svelte Frontend
- Memory + Knowledge Graph

## ✨ Author
#### Ayush Mishra