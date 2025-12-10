from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from src.state import AgentState
from src.nodes import analyze_node, respond_node

def build_graph():
    workflow = StateGraph(AgentState)

    # Nodos
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("respond", respond_node)

    # Aristas (Flujo)
    workflow.add_edge(START, "analyze")
    workflow.add_edge("analyze", "respond")
    workflow.add_edge("respond", END)

    # Memoria
    memory = MemorySaver()
    
    return workflow.compile(checkpointer=memory)