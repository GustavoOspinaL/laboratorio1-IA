from langchain_core.messages import SystemMessage, HumanMessage
from src.state import AgentState
from src.prompts import get_analysis_system_prompt, get_expert_system_prompt
from src.config import DOMAIN
from src.llm import get_llm

llm = get_llm()

def analyze_node(state: AgentState):
    messages = state["messages"]

    system_content = get_analysis_system_prompt(DOMAIN)
    
    gemini_messages = [
        {"role": "system", "content": system_content},
        *messages
    ]

    response = llm.invoke(gemini_messages)
    content_lower = response.content.lower()
    intent = "off_topic" if "fuera_de_dominio" in content_lower else "technical_query"

    print(f" Análisis completado: {response.content[:100]}...")

    return {
        "current_step": "analysis_complete",
        "analysis_results": {
            "domain": DOMAIN,
            "intent": intent,
            "confidence": 0.92,
            "details": response.content
        }
    }

def respond_node(state: AgentState):
    messages = state["messages"]
    analysis = state["analysis_results"]
    
    if analysis.get("intent") == "off_topic":
        return {
            "current_step": "response_generated",
            "messages": [{"role": "assistant", "content": f"Lo siento, mi experiencia se limita exclusivamente a {DOMAIN}. No puedo ayudarte con otros temas."}]
        }
    
    system_prompt = get_expert_system_prompt(DOMAIN, analysis['details'])

    gemini_messages = [
        {"role": "system", "content": system_prompt},
        *messages
    ]

    response = llm.invoke(gemini_messages)
    print(f"Respuesta generada: {response.content[:100]}...")

    return {
       "current_step": "response_generated",
        "messages": [{"role": "assistant", "content": response.content}]
    }