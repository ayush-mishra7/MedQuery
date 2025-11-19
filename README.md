# MedQuery – Medical Report Q&A & Summarization Engine

MedQuery is a lightweight AI-powered tool that uses LLMs to analyze medical reports and generate:
- **Question–Answer responses** based on the report
- **Short summaries**
- **Detailed clinical summaries**
- **Doctor-style structured summaries**

The backend is built using **FastAPI** and powered by **Groq’s LLaMA 3.1** model.

---

## 🚀 Features

### 🔹 Medical Q&A  
Ask any question about a medical report (diagnosis, findings, test results, etc.).

### 🔹 Multi-Level Summarization  
Automatically generate:
1. Short summary  
2. Detailed summary  
3. Doctor-style structured summary  

### 🔹 Minimal & Lightweight  
No heavy ML libraries — logic handled through LLM prompts.

---

## 📁 Project Structure

medquery/
│── requirements.txt
│── Dockerfile
│── README.md
│── app/
│ ├── main.py
│ ├── utils.py
│ ├── models.py


---

## 🔧 Installation

### 1. Create Conda environment
conda create -n medquery python=3.10 -y
conda activate medquery


### 2. Install dependencies
pip install -r requirements.txt


### 3. Add your Groq API Key  
Create a `.env` file (optional) or paste directly in `main.py`:

YOUR_API_KEY_HERE


---

## ▶️ Run the API

Use Uvicorn:
uvicorn app.main:app --reload


Open the Swagger docs:

👉 http://127.0.0.1:8000/docs

---

## 🐳 Run with Docker

### Build image:
docker build -t medquery .


### Run container:
docker run -p 8000:8000 medquery


---

## 📌 Endpoints

### **POST /qa**
Input:
```json
{
  "report": "Patient shows...",
  "question": "What is the diagnosis?"
}

POST /summarize

Input:
{
  "report": "Patient shows..."
}


~ Ayush Mishra