from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.src.schema import State

def feedback_collection_agent(state: State, llm):
    prompt = ChatPromptTemplate.from_template(
        """Analyze the following user feedback on their recent workout session:

        Current fitness plan: {current_plan}
        User feedback: {user_feedback}

        Suggest any immediate adjustments."""
    )
    chain = prompt | llm | StrOutputParser()
    feedback_summary = chain.invoke({"current_plan": state["fitness_plan"], "user_feedback": state["feedback"]})
    return state