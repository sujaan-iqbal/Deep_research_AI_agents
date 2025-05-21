from langchain_groq import ChatGroq  
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence


# Replace with your actual Groq API key
llm = ChatGroq(
    groq_api_key="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",
    model="llama3-70b-8192"
)

# Prompt template
template = """
You are an AI research assistant. Given the following research question and extracted data, generate a helpful, insightful draft response.

Research Question: {query}

Extracted Data: {data}

Draft:
"""
prompt = PromptTemplate(
    input_variables=["query", "data"],
    template=template
)

# Create a runnable pipeline (modern replacement for LLMChain)
pipeline = prompt | llm

# Draft response function
def draft_response(query, data):
    result = pipeline.invoke({"query": query, "data": data})
    return result.content if hasattr(result, "content") else result
