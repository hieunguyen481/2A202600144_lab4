import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def configure_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


load_dotenv()
configure_output()

llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
    api_key=os.getenv("OPENAI_API_KEY"),
)
response = llm.invoke("Xin chao?")
print(response.content)