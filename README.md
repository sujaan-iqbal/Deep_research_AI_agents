# 🔬 Research Assistant AI with LangGraph & LangChain

An intelligent research assistant that automates information gathering, web research, and draft generation using **LangGraph**, **LangChain**, and modern **Large Language Models (LLMs)**.

The assistant accepts a research query, searches the web for relevant information, analyzes the results, and generates a well-structured draft response. It is designed as a modular workflow that can be extended with features such as summarization, citation generation, fact-checking, and report creation.

---

## 🚀 Features

* 🌐 **Real-Time Web Research**

  * Fetches up-to-date information using the Tavily Search API.

* 🧠 **LLM-Powered Draft Generation**

  * Uses LangChain with Groq, OpenAI, or other supported models to generate research drafts.

* 🔄 **Workflow Orchestration with LangGraph**

  * Structured multi-step research pipeline.
  * Easy to customize and extend.

* 🏗️ **Modular Architecture**

  * Separate agents and workflows for maintainability.

* 💻 **Command-Line Interface**

  * Simple and lightweight interface for running research queries.

* 🔧 **Extensible Design**

  * Easily add:

    * Summarization
    * Citation generation
    * Source validation
    * Multi-agent collaboration
    * PDF export

---

## 🏗️ System Architecture

```mermaid
flowchart LR

    U[User Query]
    T[Tavily Search]
    G[LangGraph Workflow]
    D[Drafting Agent]
    L[LLM]
    O[Research Draft]

    U --> G
    G --> T
    T --> G
    G --> D
    D --> L
    L --> O

    style U fill:#4CAF50,color:#fff
    style T fill:#FF9800,color:#fff
    style G fill:#2196F3,color:#fff
    style D fill:#9C27B0,color:#fff
    style L fill:#E91E63,color:#fff
    style O fill:#607D8B,color:#fff
```

### Research Pipeline

The assistant follows a structured agent workflow:

1. Receive research query from user
2. Search the web using Tavily
3. Collect and process relevant information
4. Pass retrieved context into LangGraph workflow
5. Generate a draft using the LLM
6. Return a structured research response

---

## ⚙️ Workflow Execution

```mermaid
sequenceDiagram

    participant User
    participant CLI
    participant LangGraph
    participant Tavily
    participant LLM

    User->>CLI: Enter Research Query
    CLI->>LangGraph: Start Workflow

    LangGraph->>Tavily: Search Query
    Tavily-->>LangGraph: Search Results

    LangGraph->>LLM: Generate Draft
    LLM-->>LangGraph: Draft Response

    LangGraph-->>CLI: Final Output
    CLI-->>User: Display Research Draft
```

---

## 🖥️ CLI Demo

```bash
$ python main.py

╔════════════════════════════════════════════╗
║      Research Assistant AI v1.0           ║
╚════════════════════════════════════════════╝

Enter your research query:

> What are the latest breakthroughs in quantum computing?

🔍 Searching the web...

✓ Retrieved 5 relevant sources

🧠 Generating draft...

✓ Draft completed

────────────────────────────────────────────

Recent breakthroughs in quantum computing
include advances in error correction,
logical qubits, and fault-tolerant systems.
Researchers at IBM, Google, and Quantinuum
have demonstrated major progress toward
scalable quantum architectures...

────────────────────────────────────────────
```

---

## 📂 Project Structure

```text
research-assistant-ai/
│
├── agents/
│   └── drafting_agent.py
│
├── workflows/
│   └── research_graph.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Future Roadmap

```mermaid
timeline
    title Research Assistant Roadmap

    section Current
        Web Search : Complete
        Draft Generation : Complete
        LangGraph Workflow : Complete

    section Next
        Source Citations : Planned
        Research Summaries : Planned
        PDF Export : Planned

    section Future
        Multi-Agent Research : Future
        Fact Checking : Future
        Academic References : Future
```
