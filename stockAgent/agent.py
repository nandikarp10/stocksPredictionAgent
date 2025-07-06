from google.adk.agents import Agent
from stockAgent.stock_tools import stock_recommendation, get_stock_price

root_agent = Agent(
    name="stock_predictor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about stock tickers."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about stocks and their curent prices and recommendations."
    ),
    tools=[stock_recommendation, 
           get_stock_price],
)

# Run the agent 
# adk web