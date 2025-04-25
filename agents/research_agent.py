# agents/research_agent.py

from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing in your environment variables")

# Initialize client
client = TavilyClient(api_key=TAVILY_API_KEY)

# Search function for use in workflows
def tavily_search(query):
    results = client.search(query=query, include_answer=True)
    return results
