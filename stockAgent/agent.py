from google.adk.agents import Agent

def get_stock_price(symbol: str) -> dict:
    """Retrieves the current stock price for a given stock symbol.

    Args:
        symbol (str): The stock symbol to retrieve the price for.

    Returns:
        dict: status and result or error msg.
    """
    if symbol.lower() == "aapl":
        return {
            "status": "success",
            "price": 150.25,
            "currency": "USD",
        }
    else:
        return {
            "status": "error",
            "error_message": f"Stock price for '{symbol}' is not available.",
        }


root_agent = Agent(
    name="stock_predictor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about stock tickers."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about stocks."
    ),
    tools=[get_stock_price]
)