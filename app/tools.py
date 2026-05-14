from langchain.tools import tool
from app.database import engine
from app.prompts import SYSTEM_PROMPT
from langchain_core.messages import HumanMessage
from sqlalchemy import text
from app.llm import llm


@tool(
    "query_customer_db",
    description="""
Use this tool ONLY for questions about the 'customers' table.

It handles:
- customer filtering (city, country)
- counting customers
- searching customer details
- credit limit queries

Input must be a natural language question.
Output is database result.
"""
)
def query_customer_db(question: str) -> str:
    messages = [SYSTEM_PROMPT]
    messages.append(HumanMessage(content=question))

    response = llm.invoke(messages)
    sql = response.content.strip()
    print(sql)
    
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()    
        data = [row[0] for row in rows]
        return {
        "count": len(rows),
        "data": [row[0] for row in rows]
        } 
