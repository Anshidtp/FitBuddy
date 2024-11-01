from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.src.schema import State

def motivational_agent(state: State, llm):
    prompt = ChatPromptTemplate.from_template(
        """Provide encouragement, tips, or reminders to the user:

        User Data: {user_data}
        Current Plan: {current_plan}
        Recent Progress: {recent_progress}"""
    )
    chain = prompt | llm | StrOutputParser()
    motivation = chain.invoke(
        {"user_data": str(state["user_data"]), "current_plan": state["fitness_plan"], "recent_progress": state["progress"][-1] if state["progress"] else ""}
    )
    return state