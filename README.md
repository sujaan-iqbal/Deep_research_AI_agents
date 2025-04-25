# Research Assistant AI with LangGraph and LangChain

This project is a research assistant tool built using LangGraph and LangChain. It allows you to input a research query, fetch relevant information from the web, and generate a draft response using a language model (LLM). This tool can be used for automating research tasks and generating academic drafts.

---

## Features

- Real-time web search using Tavily API
- Modular workflow with LangGraph for research process
- Drafting capabilities using LangChain and LLMs
- Command-line interface for ease of use
- Easily extendable for future features such as summarization and citation generation

---


---

## Project Structure

- **agents/drafting_agent.py**: Handles the drafting logic using LangChain and the language model.
- **workflows/research_graph.py**: Defines the workflow for processing the research query and generating a response.
- **main.py**: The main entry point for running the assistant.
- **requirements.txt**: Contains all the necessary dependencies for the project.
- **README.md**: This file, which explains the project.

---

## Example

When you run the program and enter a research question like "What are the latest breakthroughs in quantum computing?", the system will search for relevant information online and generate a draft response. For example:


---

## Technologies Used

- LangGraph
- LangChain
- Groq / OpenAI LLMs
- Tavily API for web searches
- Python 3.10 or higher

---


## Contributing

If you would like to contribute to this project, feel free to open a pull request. Suggestions for new features or improvements are always welcome.

---

## License

This project is licensed under the MIT License. You are free to use and modify it as per the terms of the license.
