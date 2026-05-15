from langchain.agents import  create_agent
from app.tools import query_customer_db
from app.llm import llm
from app.prompts import SYSTEM_PROMPT

tools = [query_customer_db]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "List all the customer names from USA."
        }
    ]
})

raw = result["messages"][-1].content
print(raw)
