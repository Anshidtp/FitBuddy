from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json
from app.src.schema import State


def routine_generation_agent(state: State, llm):
    prompt = ChatPromptTemplate.from_template(
        """You are an AI fitness coach. Create a personalized fitness routine based on the following user data:

        {user_data}

        Create a detailed weekly fitness plan that includes:
        1. Types of exercises
        2. Duration and frequency of workouts
        3. Intensity levels
        4. Rest days
        5. Any dietary recommendations"""
    )
    chain = prompt | llm | StrOutputParser()
    plan = chain.invoke({"user_data": json.dumps(state["user_data"])})
    state["fitness_plan"] = plan
    return state