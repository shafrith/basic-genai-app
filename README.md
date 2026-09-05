# 🤖 AI Chatbot — Streamlit & LangChain

> **A smart, conversational AI assistant built with Python, LangChain, Streamlit, and OpenAI.**

An interactive web-based AI chatbot that demonstrates how **Generative AI, conversational memory, and real-time response streaming** can be combined to create a smooth and engaging chat experience.

The application remembers previous messages within the conversation, allowing users to have natural **multi-turn conversations** instead of starting from scratch with every question.

---

## ✨ Features

| Feature                      | Description                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| 💬 **Interactive Chat**      | Modern web-based chat interface powered by Streamlit            |
| 🧠 **Conversational Memory** | Maintains chat history for context-aware conversations          |
| ⚡ **Real-Time Streaming**   | Displays AI responses progressively for a responsive experience |
| 🤖 **OpenAI Powered**        | Uses `gpt-4o-mini` for fast and high-quality responses          |
| 🔐 **Secure API Key**        | Loads the OpenAI API key securely using `.env`                  |
| 🐍 **Python + LangChain**    | Simple and extensible GenAI application architecture            |

---

## 🧠 How It Works

The chatbot follows a simple conversational flow:

```text
        👤 User
           │
           ▼
    ┌───────────────┐
    │   Streamlit   │
    │  Chat Interface│
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │ Chat History  │
    │    / Memory   │
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │   LangChain   │
    │ Prompt + LLM  │
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │    OpenAI     │
    │  gpt-4o-mini  │
    └───────┬───────┘
            │
            ▼
       ⚡ Streaming
            │
            ▼
        👤 User
```

---

## 🛠️ Technology Stack

### Core Technologies

- 🐍 **Python**
- 🦜 **LangChain**
- 🤖 **OpenAI**
- 🎨 **Streamlit**
- 🔐 **python-dotenv**

### Key Libraries

```text
langchain
langchain-openai
streamlit
python-dotenv
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have:

- **Python 3.8+**
- An **OpenAI API Key**
- `pip` installed and available in your terminal

Get your API key from [OpenAI Platform](https://platform.openai.com/?utm_source=chatgpt.com).

---

### 2️⃣ Create the Project

Create a project folder and navigate into it:

```bash
mkdir basic-genai-app
cd basic-genai-app
```

---

### 3️⃣ Install Dependencies

Install the required packages:

```bash
pip install langchain langchain-openai python-dotenv streamlit
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-actual-api-key-here
```

> 🔐 **Important:** Never commit your `.env` file to GitHub or share your API key publicly.

Add `.env` to your `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

---

### 5️⃣ Add the Application

Create a file named:

```text
main.py
```

Add your Streamlit + LangChain chatbot implementation to this file.

---

## ▶️ Run the Application

Since this is a **Streamlit application**, don't run it using:

```bash
python main.py
```

Instead, start the Streamlit server with:

```bash
streamlit run main.py
```

Once started, Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser and start chatting with your AI assistant. 🚀

---

## 💬 Example Conversation

```text
👤 User:
What is Generative AI?

🤖 AI:
Generative AI refers to artificial intelligence systems
that can create new content such as text, images, audio,
video, and code.

👤 User:
Can you give me a simple example?

🤖 AI:
Sure! ChatGPT is an example of a Generative AI application
that can generate human-like text based on user prompts.
```

Because the chatbot maintains **conversation history**, follow-up questions can use information from earlier messages.

---

## 📁 Project Structure

```text
basic-genai-app/
│
├── 📄 main.py              # Streamlit + LangChain application
├── 🔐 .env                 # OpenAI API key (local only)
├── 🛡️ .gitignore           # Files excluded from Git
├── 📖 README.md            # Project documentation
└── 📁 __pycache__/         # Python generated files
```

---

## 🔐 Security

Never expose your OpenAI API key in source code.

❌ **Avoid:**

```python
api_key = "sk-xxxxxxxxxxxxxxxx"
```

✅ **Use environment variables:**

```env
OPENAI_API_KEY=your-api-key
```

And load it using `python-dotenv`.

> **Always make sure `.env` is included in `.gitignore`.**

---

## 🎯 What This Project Demonstrates

This project provides a practical introduction to:

- Generative AI application development
- LangChain fundamentals
- OpenAI LLM integration
- Prompt and message management
- Conversational memory
- Streaming LLM responses
- Streamlit application development
- Environment variable management

---

## 🌟 Future Enhancements

Possible improvements include:

- 📚 **RAG** — Chat with PDFs and documents
- 💾 **Persistent Chat History** — Store conversations across sessions
- 🔎 **Web Search** — Retrieve real-time information
- 👥 **Multi-User Conversations** — Separate user sessions
- 📊 **LangSmith Integration** — Trace and monitor LLM calls
- 🎨 **Custom Chat UI** — Add themes and advanced controls

---

## 📌 Project Summary

**AI Chatbot** is a lightweight Generative AI application that combines **Streamlit's interactive UI**, **LangChain's orchestration capabilities**, **conversational memory**, and **OpenAI's language model** to provide a responsive multi-turn AI chat experience.

> 🚀 **Built to learn. Designed to experiment. Ready to extend.**
