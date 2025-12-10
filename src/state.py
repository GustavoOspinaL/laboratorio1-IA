from typing import TypedDict, Annotated, Sequence
import operator

class AgentState(TypedDict):
  messages: Annotated[Sequence[dict], operator.add]
  current_step: str
  analysis_results: dict