# PDF Query with AstraDB using LangChain

This project demonstrates a **retrieval-augmented generation (RAG) pipeline** that allows querying a PDF using natural language. It leverages **LangChain**, **OpenAI embeddings**, and **AstraDB (Cassandra)** to provide answers grounded in the document content.

You can ask questions interactively, and the system retrieves relevant chunks from the PDF and generates a contextual answer using an LLM.

---

## Features

- Load PDFs and extract text
- Split text into chunks for embedding
- Store embeddings in AstraDB (Cassandra)
- Query documents using natural language questions
- Use LangChain components for retrieval, embeddings, and LLM interaction
- Optional support for Hugging Face datasets for additional content

---

## LangChain Components Used

- `langchain_community.vectorstores.Cassandra` — Vector store integration with AstraDB  
- `langchain_openai.ChatOpenAI` — LLM interface  
- `langchain_openai.OpenAIEmbeddings` — Convert text into embeddings  
- `langchain_text_splitters.RecursiveCharacterTextSplitter` — Split large documents into chunks  
- `cassio` — Initialize and manage AstraDB connection  
- `datasets` — Optional dataset loading from Hugging Face