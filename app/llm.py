from langchain_openrouter import ChatOpenRouter
from app.settings import settings

llm = ChatOpenRouter(
    model="auto",
    api_key=settings.OPENROUTER_API_KEY,
    temperature = 0,
)







