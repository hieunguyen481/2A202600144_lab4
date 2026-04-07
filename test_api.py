import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini",
                 api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke("Xin chao?")
print(response.content)
