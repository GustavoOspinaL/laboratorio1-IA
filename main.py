from langchain_core.messages import HumanMessage
from src.config import DOMAIN
from src.graph import build_graph
from src.queries import retrieve_input, save_input
import uuid

def main():
    # 1. Inicializar el grafo
    app = build_graph()
    
    # 2. Configuración de ejecución
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    print("-" * 50)
    print(f"Se ha iniciado el Agente {DOMAIN}.")
    print("-" * 50)

    while True:
        user_input = input("\nTú: ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Hasta luego.")
            break
        
        data = retrieve_input(user_input)

        if data and 'response' in data[0]:
            response = data[0]['response']
            print(f"\nAgente {DOMAIN}: {response}")
        else:
            # 3. Estado inicial
            initial_state = {
                "messages": [{"role": "user", "content": user_input}],
                "current_step": "initial",
                "analysis_results": {}
            }

            result = app.invoke(initial_state, config=config)
            
            last_message = result["messages"][-1]["content"]
            save_input(user_input, last_message)
            print(f"\nAgente {DOMAIN}: {last_message}")

if __name__ == "__main__":
    main()