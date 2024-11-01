from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json
from app.src.schema import State

def user_input_agent(state: State, llm):
    prompt = ChatPromptTemplate.from_template(
        """You are an AI fitness coach assistant. Process the following user information:

        {user_input}

        Create a structured user profile based on this information. Include all relevant details for creating a personalized fitness plan.
        Return the profile as a valid JSON string."""
    )
    chain = prompt | llm | StrOutputParser()
    user_profile = chain.invoke({"user_input": json.dumps(state["user_data"])})
    
    try:
        state["user_data"] = json.loads(user_profile)
    except json.JSONDecodeError:
        pass  
    return state