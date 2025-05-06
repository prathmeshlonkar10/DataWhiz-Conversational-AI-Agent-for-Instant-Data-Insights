# 💬 DataWhiz: Conversational AI Agent for Instant Data Insights
- Project Type: Personal Project
- Timeline: February 2025

## 🧠 Overview
DataWhiz is a conversational AI agent that transforms the way users interact with their data. Instead of writing code or scrolling through spreadsheets, users can simply upload a CSV file and ask questions in natural language to gain real-time insights. Built with cutting-edge LLM technology, DataWhiz bridges the gap between data and intuition — making data science feel like a conversation.

##✨ Key Features
- 📁 CSV Upload Support – Upload any structured CSV file for analysis

- 💬 Chat Interface – GPT-style chat window for interactive dialogue with your data

- 📊 Textual + Tabular Responses – Get answers as plain language and formatted tables

- ⚡ Instant Feedback – Results generated in real-time using OpenAI + LangChain pipelines

- 🧼 Clean & Minimal UI – Designed using Streamlit for ease and accessibility

## 🏗️ Under the Hood
### 🔄 Data Ingestion
- Parses and validates user-uploaded CSV files using Pandas

- Extracts column names, types, and value distributions for prompt context

### 🧠 AI Agent Framework
- Built using LangChain Agents powered by OpenAI GPT-4 API

- Incorporates tool chaining to dynamically query and process dataset content

### 🗣️ Natural Language Processing
- Converts user questions to data queries

- Generates human-readable responses or filtered outputs

### 📈 Future Enhancements
- Visual insights with Matplotlib/Altair integration

- Multi-source data ingestion (e.g., DBMS, cloud connectors)

- Context retention across multi-turn conversations

- DeepSeek or RAG-based upgrades for longer CSVs and better reasoning

## 🚀 Why I Built It
After working with RAG frameworks and LLMs during my internship at Tenable, I became deeply curious about AI Agents and their potential in automating data science workflows. I built DataWhiz to explore:

- How far LLMs can go in replacing code-driven data exploration

- The UI/UX aspects of a no-code data assistant

- The possibilities for scaling agent-based architecture in future tools

## 📦 Sample Use Cases (Prompts)
- "What’s the average transaction value per customer?"

- "List the top 5 products by sales volume."

- "How many entries are missing in the 'region' column?"

- "Show me a breakdown of revenue by month."


## 📈 Metrics & Performance
- Supports CSVs with 10,000+ rows without crashing

- Average response latency: ~5 seconds per query

- Successfully tested on datasets from finance, sales, and HR domains

- Handles diverse column types: numeric, categorical, date/time

## 🧪 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![LangChain – Agent orchestration + tool integration](https://img.shields.io/badge/LangChain-1C3C3C.svg?style=for-the-badge&logo=LangChain&logoColor=white)
![OpenAI GPT-4 – Natural language understanding and generation](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![Streamlit – Fast, clean front-end for interaction](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas – Data handling and transformations](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Sample Snippets
![Screenshot 2025-02-22 222057](https://github.com/user-attachments/assets/123771cb-3fbe-4929-b256-65555f3a13be)

