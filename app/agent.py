from langchain.agents import  create_agent
from app.tools import query_customer_db
from app.llm import llm
from app.structured_output import ModelResponse
import json

tools = [query_customer_db]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a PostgreSQL Text-to-SQL assistant.

RULES:
- Use ONLY the tool: query_customer_db
- Do not hallucinate or guess data
- Only work with customer-related data
- Always produce valid structured output

    """
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "How many customers are provided with both of their address lines?"
        }
    ]
})

raw = result["messages"][-1].content
print(raw)
