from langchain.agents import  create_agent
from app.tools import query_customer_db
from app.llm import llm

tools = [query_customer_db]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a SQL assistant for PostgreSQL.

    Rules:
    - Only use query_customer_db tool
    - Only read customer-related data
    - Return clean answers
    - Do not fabricate data

    """
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Show customer names of customers from USA"
        }
    ]
})


print(result)
