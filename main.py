import os
from workflows.research_graph import compiled_graph
from dotenv import load_dotenv

load_dotenv()  # Load .env vars

if __name__ == "__main__":
    query = input("Enter your research question: ")
    result = compiled_graph.invoke({"query": query})
    print("\n=== Final Answer ===\n")
    print(result)
