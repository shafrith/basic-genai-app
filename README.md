Basic GenAI Chatbot

A beginner-friendly, interactive web-based chatbot built using Python, LangChain, and Streamlit. This project demonstrates how to build a generative AI application that features conversational memory and real-time text streaming.

🌟 Features

Interactive Web UI: Provides a clean, modern chat interface using Streamlit.

Conversational Memory: Uses LangChain's message history to remember previous interactions within the session, allowing for natural, multi-turn conversations.

Real-time Streaming: Displays the AI's responses token-by-token (a "typewriter" effect) for a faster and more engaging user experience.

OpenAI Integration: Powered by OpenAI's gpt-4o-mini model.

🛠️ Tech Stack

Python: The core programming language.

LangChain (langchain, langchain-openai): The framework used to connect to the LLM and manage chat history and streaming.

Streamlit (streamlit): The web framework used to build the front-end user interface.

Dotenv (python-dotenv): Manages secure loading of API keys.

📋 Prerequisites

Before running this application, you will need:

Python 3.8 or higher installed on your machine.

An OpenAI API Key.

🚀 Installation & Setup

Set up the project folder:
Create a folder named basic-genai-app and navigate into it.

Install dependencies:
Open your terminal and run the following command to install the required Python packages:

pip install langchain langchain-openai python-dotenv streamlit

Configure your API Key:
Create a file named .env in the root of your project folder and add your OpenAI API key:

OPENAI_API_KEY=your-actual-api-key-here

(Note: Ensure your .env file is added to your .gitignore so you do not accidentally expose your API key.)

Add the application code:
Ensure your main.py file contains the Streamlit and LangChain integration code.

💻 How to Run

Because this is a Streamlit web application, you cannot run it with the standard python main.py command.

To launch the app, run the following command in your terminal:

streamlit run main.py

This will start a local server and automatically open a new tab in your default web browser (usually at http://localhost:8501) where you can start chatting with your AI!

📂 Project Structure

basic-genai-app/
│
├── .env # Stores your secure API keys (DO NOT commit to version control)
├── .gitignore # Tells Git which files to ignore (must include .env)
├── main.py # The main application script containing LangChain and Streamlit code
└── README.md # Project documentation
