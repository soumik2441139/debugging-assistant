# AI Debugging Assistant

An AI-powered web application that analyzes Python code and error logs and provides debugging assistance using LLM APIs.

---

# Architecture Diagram

```mermaid
flowchart TD
    A[User Browser] --> B[Custom Domain - GoDaddy DNS]
    B --> C[Azure App Service]
    C --> D[Streamlit Application]
    D --> E[Groq API]
    D --> F[Google Gemini API]
```

---

# Deployment Flow

```mermaid
sequenceDiagram
    participant User
    participant DNS
    participant Azure
    participant App
    participant LLM

    User->>DNS: Request www.domain.shop
    DNS->>Azure: Resolve CNAME to Azure
    Azure->>App: Route traffic
    App->>LLM: Send code for debugging
    LLM-->>App: Return suggestions
    App-->>User: Display results
```

---

# System Components

```mermaid
graph LR
    UI[Streamlit UI]
    Backend[Python Backend]
    Config[Environment Variables]
    LLM[LLM APIs]

    UI --> Backend
    Backend --> LLM
    Backend --> Config
```

---

# Project Structure

```plaintext
.
├── apps/
├── config/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

---

# Tech Stack

* Python 3.12
* Streamlit
* Groq API
* Google Generative AI
* Azure App Service
* Custom Domain (GoDaddy)
* SSL (Azure Managed Certificate)

---
