from typing import TypedDict
from langgraph.graph import StateGraph

from agents.research_agent import tavily_search
from agents.drafting_agent import draft_response

class ResearchState(TypedDict):
    query: str
    data: str
    draft: str

graph = StateGraph(state_schema=ResearchState)

graph.add_node("start", lambda state: state)

graph.add_node("fetch", lambda state: {
    "query": state["query"],
    "data": tavily_search(state["query"])
})

# ✅ Fix: Renamed node from "draft" to "draft_node"
graph.add_node("draft_node", lambda state: {
    "query": state["query"],
    "data": state["data"],
    "draft": draft_response(state["query"], state["data"])

})

graph.add_edge("start", "fetch")
graph.add_edge("fetch", "draft_node")

graph.set_entry_point("start")
graph.set_finish_point("draft_node")

compiled_graph = graph.compile()
