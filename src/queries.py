from src.database import execute_insert, execute_select

def save_input(value: str, response: str):
    query = """
    INSERT INTO AgentLangGraph.inputs (input, response) 
    VALUES (%s, %s);
    """
    execute_insert(query, (value, response))

def retrieve_input(value: str):
   response = execute_select(f"SELECT response FROM AgentLangGraph.inputs WHERE input = '{value}';")
   return response