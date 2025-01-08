from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.model.groq import Groq
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.tools.yfinance import YFinanceTools
from typing import Union
import time
import os 


tools = {
    "DuckDuckGo": [DuckDuckGo()],
    "Arxiv tool": [ArxivToolkit()],
    "YFinance tool": [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)]
}

def ollama_model_api(
        model_id: str = "gemma2:2b", 
        query_prompt: str = "",
        instructions: str = "",
        *,
        tool_name: str | None) -> Union[str, float]:
    
    if tool_name is None:
        agent = Agent(
            model=Ollama(id=model_id),
            markdown=True,
            instructions=instructions,
        )
    else:
        agent = Agent(
            model=Ollama(id=model_id),
            markdown=True,
            instructions=instructions,
            tools=tools[tool_name]
        )

    start = time.time()

    run: RunResponse = agent.run(query_prompt)

    api_latency = (time.time() - start) * 1000

    return str(run.content), float(api_latency)

def gemini_model_api(
        model_id: str = "gemini-1.5-flash", 
        query_prompt: str = "",
        instructions: str = "",
        *,
        tool_name: str | None) -> Union[str, float]:

    if tool_name is None:
        agent = Agent(
            model=Gemini(id=model_id),
            markdown=True,
            instructions=instructions,
        )
    else:
        agent = Agent(
            model=Gemini(id=model_id),
            markdown=True,
            instructions=instructions,
            tools=tools[tool_name]
        )

    start = time.time()

    run: RunResponse = agent.run(query_prompt)

    api_latency = (time.time() - start) * 1000

    return str(run.content), float(api_latency)


def groq_model_api(
        model_id: str = "gemma2-9b-it",
        query_prompt: str = "",
        instructions: str = "",
        *,
        tool_name: str | None) -> Union[str, float]:

    if tool_name is None:
        agent = Agent(
            model=Groq(id=model_id),
            markdown=True,
            instructions=instructions,
        )
    else:
        agent = Agent(
            model=Groq(id=model_id),
            markdown=True,
            instructions=instructions,
            tools=tools[tool_name]
        )

    start = time.time()

    run: RunResponse = agent.run(query_prompt)

    api_latency = (time.time() - start) * 1000

    return str(run.content), float(api_latency)

# if __name__ == "__main__":
#     print(gemini_model_api(prompt="what is 2+2 ?"))