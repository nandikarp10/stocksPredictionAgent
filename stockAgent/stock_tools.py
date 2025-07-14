import yfinance as stockData


def stock_recommendation(stock_ticker: str) -> str:
    """
    Function to provide stock recommendation based on moving averages.
    Args:
        stock_ticker (str): The stock ticker symbol to analyze. 
    Returns:
        str: Recommendation based on the stock's moving averages.
    """
    try:
        # Get Stock Data for 2 year
        stock = stockData.Ticker (stock_ticker)
        history = stock.history (period = "2y")

        # Calculate the moving averages of the stock ticker
        history['SMA_200'] = history['Close'].rolling(window=200).mean()
        history['SMA_365'] = history['Close'].rolling(window=365).mean()

        # Get latest stock closing price - dropna removes rows with missing/empty values
        history = history.dropna(subset = ['SMA_200','SMA_365'])
        if history.empty:
            return f"Not enough data to compute moving averages for {stock_ticker}."
        latest = history.iloc[-1]
        latest_close = latest['Close']
        latest_sma_365 = latest['SMA_365']
        latest_sma_200 = latest['SMA_200']

        # Logic for recommendation

        if latest_sma_200 > latest_sma_365 and latest_close > latest_sma_200:
            return f"Buy recommendation for {stock_ticker}: The stock is in an uptrend."
        elif latest_sma_200 < latest_sma_365 and latest_close < latest_sma_200:
            return f"Sell recommendation for {stock_ticker}: The stock is in a downtrend."
        else:
            return f"Hold recommendation for {stock_ticker}: The stock is in a consolidation phase."
        
    except Exception as e:
        return f"Error fetching data for {stock_ticker}: {e}"


def get_stock_price(stock_ticker: str) -> str:
    """
    Function to get the current stock price.
    Args:
        stock_ticker (str): The stock ticker symbol to fetch the price for.
    Returns:
        str: Current stock price or an error message.
    """
    try:
        stock = stockData.Ticker(stock_ticker)
        current_price = stock.history(period="1d")['Close'].iloc[-1]
        return f"The current price of {stock_ticker} is ${current_price:.2f}."
    except Exception as e:
        return f"Error fetching price for {stock_ticker}: {e}"   
    
# get the company name and summary for a stock ticker using yfinance
def get_company_summary(stock_ticker: str) -> str:
    """
    Function to get the company name and summary for a stock ticker.
    Args:
        stock_ticker (str): The stock ticker symbol to fetch the company information for.
    Returns:
        str: Company name and summary or an error message.
    """
    try:
        stock = stockData.Ticker(stock_ticker)
        company_info = stock.info
        company_name = company_info.get('longName', 'N/A')
        company_summary = company_info.get('longBusinessSummary', 'No summary available.')
        return f"{company_name}\n {company_summary}"
    except Exception as e:
        return f"Error fetching company information for {stock_ticker}: {e}"