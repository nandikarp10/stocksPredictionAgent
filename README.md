# Stocks Prediction Agent

![Stock Agent Chat](Stock%20Agent%20Chat.png)

This project is a Stocks Prediction Agent that answers questions about stock tickers, provides current prices, and gives recommendations based on moving averages using AI and financial data.

## Features

- Get current stock prices using Yahoo Finance
- Receive buy/hold/sell recommendations based on moving averages
- AI-powered agent interface (Google ADK)
- Easy-to-extend toolset

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/stocksPredictionAgent.git
   cd stocksPredictionAgent
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   Or, if using pyproject.toml:
   ```
   pip install .
   ```

3. Set up your environment variables in `stockAgent/.env` if needed.

## Usage

1. Run the agent using Google ADK:
   ```
   adk web
   ```
2. Ask questions about stock tickers, e.g.:
   - "What is the current price of AAPL?"
   - "Should I buy TSLA?"

## Project Structure

- `stockAgent/agent.py`: Main agent definition
- `stockAgent/stock_tools.py`: Stock price and recommendation tools
- `pyproject.toml`: Project metadata and dependencies

## Requirements

- Python 3.9+
- google-adk
- yfinance

## License

MIT License

---

*For more details, see the code in `stockAgent/agent.py` and `stockAgent/stock_tools.py`.*
