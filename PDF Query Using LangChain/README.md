# 📄 PDF Insight: AI-Powered Document Query System

A professional-grade **Retrieval-Augmented Generation (RAG)** pipeline designed to perform semantic search and question-answering against PDF documents. This project demonstrates the integration of vector databases with Large Language Models (LLMs) to eliminate hallucinations and provide fact-based responses.

---

## System Architecture

The system follows the modern RAG architecture to bridge the gap between static PDF data and dynamic LLM reasoning:

1.  **Ingestion:** Extracts text from PDFs using `PyPDF2`.
2.  **Chunking:** Breaks text into overlapping segments using `RecursiveCharacterTextSplitter` to preserve local context.
3.  **Vectorization:** Converts text chunks into high-dimensional embeddings via OpenAI's `text-embedding-ada-002`.
4.  **Storage:** Indexes embeddings in a **FAISS** (Facebook AI Similarity Search) vector database.
5.  **Retrieval:** Performs a similarity search to find the most relevant document chunks for a user's query.
6.  **Augmentation:** "Stuffs" retrieved chunks into a structured prompt via `create_stuff_documents_chain`.
7.  **Generation:** Produces a final answer using GPT models based *only* on the provided context.



---

## Tech Stack

* **Orchestration:** LangChain (LCEL & Modern Chains)
* **LLM:** OpenAI (GPT-3.5-Turbo / GPT-4)
* **Vector Database:** FAISS
* **Embeddings:** OpenAI Embeddings
* **Environment:** Python 3.10+ / Anaconda

---

## Key Technical Features

* **Contextual Integrity:** Uses structured XML-style delimiters (`<context>`) in prompts to prevent instruction injection.
* **Hallucination Guardrails:** Explicitly programmed to decline answering if the information is missing from the source PDF.
* **Efficient Retrieval:** Optimized search parameters to balance speed and accuracy in document lookup.

