from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from openai import AuthenticationError, OpenAIError
from typing_extensions import TypedDict

from tools import calculate_budget, search_flights, search_hotels


load_dotenv()


def configure_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def safe_print(message: str) -> None:
    try:
        print(message)
    except UnicodeEncodeError:
        fallback = message.encode("ascii", errors="replace").decode("ascii")
        print(fallback)

BASE_DIR = Path(__file__).resolve().parent
SYSTEM_PROMPT_PATH = BASE_DIR / "system_prompt.txt"
SYSTEM_PROMPT = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


TOOLS = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
    api_key=os.getenv("OPENAI_API_KEY"),
)
llm_with_tools = llm.bind_tools(TOOLS)


def agent_node(state: AgentState) -> AgentState:
    messages = state["messages"]
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = llm_with_tools.invoke(messages)
    has_tool_results = any(isinstance(message, ToolMessage) for message in messages)

    tool_calls = getattr(response, "tool_calls", [])
    if tool_calls:
        for tool_call in tool_calls:
            safe_print(f"[Tool] {tool_call['name']} -> {tool_call['args']}")
    elif has_tool_results:
        safe_print("[Agent] Khong goi them tool, dang tao cau tra loi cuoi cung.")
    else:
        safe_print("[Agent] Tra loi truc tiep ngay tu dau, khong can goi tool.")

    return {"messages": [response]}


builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition, {"tools": "tools", END: END})
builder.add_edge("tools", "agent")

graph = builder.compile()


if __name__ == "__main__":
    configure_output()
    safe_print("=" * 60)
    safe_print("TravelBuddy - Tro ly Du lich Thong minh")
    safe_print("Go 'quit' de thoat")
    safe_print("=" * 60)

    while True:
        user_input = input("\nBan: ").strip()
        if user_input.lower() in {"quit", "exit", "q"}:
            safe_print("Tam biet!")
            break

        if not user_input:
            safe_print("TravelBuddy: Ban hay nhap noi dung can tu van nhe.")
            continue

        safe_print("\nTravelBuddy dang suy nghi...")
        try:
            result = graph.invoke({"messages": [("human", user_input)]})
            final_message = result["messages"][-1]
            safe_print(f"\nTravelBuddy: {final_message.content}")
        except AuthenticationError:
            safe_print(
                "\nTravelBuddy: API key khong hop le. Hay kiem tra lai file .env "
                "va thu chay test_api.py truoc."
            )
        except OpenAIError as error:
            safe_print(f"\nTravelBuddy: Loi khi goi OpenAI API: {error}")
