from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

# State definition
class State(TypedDict):
    user_data: dict
    fitness_plan: str
    feedback: str
    progress: List[str]
    messages: Annotated[list, add_messages]