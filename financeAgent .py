from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import re

load_dotenv()  # loads api keys

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),  # llm model of agent
    tools=[YFinanceTools(
        stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data"]
)
inp1 = list(
    input("company names with space in between, provide symbols: ").split())

agent.print_response(
    f"Summarize and compare analyst recommendations and fundamentals of {inp1}")
