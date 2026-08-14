# AI Resume Analyzer using RAG

An AI-powered Resume Analyzer that allows users to upload a resume and ask questions based on its content. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the uploaded resume and generate accurate responses using Gemini.

## 🚀 Project Overview

Recruiters and interviewers often spend a significant amount of time reviewing resumes and preparing questions from candidate profiles.

This project aims to reduce that effort by allowing users to upload a resume and interact with it using natural language.

The system extracts the resume content, divides it into smaller chunks, converts the chunks into embeddings, stores them in a FAISS vector database, and retrieves the most relevant information whenever a question is asked.

The retrieved information is then provided to Gemini to generate the final response.

## 🎯 Problem Statement

Manually analyzing resumes and finding relevant information can be time-consuming.

This project provides an AI-based solution that can:

- Analyze uploaded resumes
- Search resume content semantically
- Answer questions based on the resume
- Retrieve relevant information quickly
- Reduce unnecessary manual resume analysis

## ✨ Features

- 📄 Upload PDF resumes
- 🔍 Semantic search
- 🤖 AI-powered question answering
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Resume text chunking
- 🔢 Text embeddings
- ⚡ FAISS vector search
- 🌐 Streamlit interface
- 🔐 Environment-based API key management

## 🏗️ Architecture

```text
                Resume PDF
                    │
                    ▼
              PDF Text Loader
                    │
                    ▼
                 Chunking
                    │
                    ▼
          Sentence Transformer
             Embeddings
                    │
                    ▼
              FAISS Vector Store
                    │
                    │
User Question ──────┘
      │
      ▼
Question Embedding
      │
      ▼
Semantic Search
      │
      ▼
Relevant Resume Chunks
      │
      ▼
       Gemini LLM
      │
      ▼
   Final Answer
