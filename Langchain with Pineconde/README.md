# 📄 AI-Powered PDF Assistant: RAG with LangChain & Pinecone

An intelligent document assistant built as part of my MSc portfolio. This project implements a **Retrieval-Augmented Generation (RAG)** pipeline to chat with PDF documents, specifically optimized for extracting information from visa and immigration status documents.

## 🚀 Key Features
- **Intelligent Chunking:** Uses `RecursiveCharacterTextSplitter` to ensure contextual integrity.
- **Vector Search:** Powered by **Pinecone** (Serverless) for high-performance cloud retrieval.
- **Modern LLM Integration:** Utilizes OpenAI's `gpt-4o-mini` via the latest LangChain v1.0+ standards.
- **Production-Grade QA:** Implements the `load_qa_chain` ("Stuff" method) for accurate, context-aware answering.

## 🛠️ Tech Stack
- **Orchestration:** LangChain (v1.0+)
- **Large Language Model:** OpenAI GPT-4o-mini
- **Vector Database:** Pinecone
- **Embeddings:** OpenAI `text-embedding-3-small`
- **Language:** Python 3.10+

## 📐 Project Architecture
1. **Ingestion:** PDF files are loaded using `PyPDFDirectoryLoader`.
2. **Chunking:** Documents are split into 1000-character segments with a 100-character overlap.
3. **Embedding:** Chunks are converted into 1536-dimensional vectors.
4. **Storage:** Vectors are upserted into a Pinecone Index.
5. **Retrieval:** User queries are embedded and compared against the vector store.
6. **Generation:** Relevant chunks are "stuffed" into the LLM prompt to generate the final answer.