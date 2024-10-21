import requests
import os
from langchain_core.tools import tool

API_KEY = os.getenv("FMP_API_KEY")

BASE_URL = "https://financialmodelingprep.com/api"


def _get(endpoint, **kwargs):
    """
    Helper function to make a GET request to the FMP API.
    
    Args:
        endpoint (str): The API endpoint to call.
        kwargs: Additional query parameters to include in the request.
    
    Returns:
        dict: The JSON response from the API.
    """
    kwargs['apikey'] = API_KEY
    response = requests.get(f"{BASE_URL}/{endpoint}", params=kwargs)
    response.raise_for_status()  # Raises HTTPError, if one occurred
    return response.json()

@tool
def search_company(query, limit=10, exchange=None):
    """
    Search for a company by name or symbol.
    
    Args:
        query (str): The search query (company name or symbol). [Required]
        limit (int, optional): Maximum number of results to return. @tool
default is 10.
        exchange (str, optional): The exchange to filter by.
    
    Returns:
        dict: A list of search results with company details.
    """
    request_params = {
        "query": query,
        "limit": limit
    }
    if exchange:
        request_params["exchange"] = exchange
    return _get("v3/search", **request_params)

@tool
def get_company_profile(symbol):
    """
    Get the profile information of a company by its stock symbol.
    
    Args:
        symbol (str): The stock symbol. [Required]
    
    Returns:
        dict: Company profile details.
    """
    return _get(f"v3/profile/{symbol}")

@tool
def get_stock_quote(symbol):
    """
    Get the real-time stock quote for a given symbol.
    
    Args:
        symbol (str): The stock symbol. [Required]
    
    Returns:
        dict: Real-time quote data.
    """
    return _get(f"v3/quote/{symbol}")

@tool
def get_income_statement(symbol, period="annual"):
    """
    Get the income statement for a given company.
    
    Args:
        symbol (str): The stock symbol. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Income statement data for the company.
    """
    return _get(f"v3/income-statement/{symbol}", period=period)

@tool
def get_balance_sheet(symbol, period="annual"):
    """
    Get the balance sheet for a given company.
    
    Args:
        symbol (str): The stock symbol. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Balance sheet data for the company.
    """
    return _get(f"v3/balance-sheet-statement/{symbol}", period=period)

@tool
def get_cash_flow(symbol, period="annual"):
    """
    Get the cash flow statement for a given company.
    
    Args:
        symbol (str): The stock symbol. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Cash flow data for the company.
    """
    return _get(f"v3/cash-flow-statement/{symbol}", period=period)

@tool
def get_market_cap(symbol):
    """
    Get the market capitalization of a given company.
    
    Args:
        symbol (str): The stock symbol. [Required]
    
    Returns:
        dict: Market capitalization data for the company.
    """
    return _get(f"v3/market-capitalization/{symbol}")

@tool
def get_analyst_estimates(symbol):
    """
    Get the analyst estimates for a given company.
    
    Args:
        symbol (str): The stock symbol. [Required]
    
    Returns:
        dict: Analyst estimates for the company.
    """
    return _get(f"v3/analyst-estimates/{symbol}")

@tool
def get_bulk_quote(symbols):
    """
    Get stock quotes for multiple symbols at once.
    
    Args:
        symbols (list of str): List of stock symbols. [Required]
    
    Returns:
        dict: Quotes for the given symbols.
    """
    symbols_str = ','.join(symbols)
    return _get(f"v3/quote/{symbols_str}")

@tool
def get_bulk_income_statements(year, period="annual"):
    """
    Get income statements in bulk for a specific year.
    
    Args:
        year (int): The year for which to get income statements. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Bulk income statement data.
    """
    return _get("v4/income-statement-bulk", year=year, period=period)

@tool
def get_bulk_balance_sheets(year, period="annual"):
    """
    Get balance sheets in bulk for a specific year.
    
    Args:
        year (int): The year for which to get balance sheets. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Bulk balance sheet data.
    """
    return _get("v4/balance-sheet-statement-bulk", year=year, period=period)

@tool
def get_bulk_cash_flows(year, period="annual"):
    """
    Get cash flow statements in bulk for a specific year.
    
    Args:
        year (int): The year for which to get cash flows. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Bulk cash flow data.
    """
    return _get("v4/cash-flow-statement-bulk", year=year, period=period)

@tool
def get_bulk_ratios(year, period="annual"):
    """
    Get financial ratios in bulk for a specific year.
    
    Args:
        year (int): The year for which to get ratios. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Bulk financial ratios data.
    """
    return _get("v4/ratios-bulk", year=year, period=period)

@tool
def get_bulk_key_metrics(year, period="annual"):
    """
    Get key financial metrics in bulk for a specific year.
    
    Args:
        year (int): The year for which to get key metrics. [Required]
        period (str, optional): The period type ("annual" or "quarterly"). @tool
default is "annual".
    
    Returns:
        dict: Bulk key financial metrics data.
    """
    return _get("v4/key-metrics-bulk", year=year, period=period)

@tool
def get_forex_pairs():
    """
    Get a list of available forex currency pairs.
    
    Returns:
        dict: Available forex currency pairs.
    """
    return _get("v3/symbol/available-forex-currency-pairs")

@tool
def get_forex_quote(symbol):
    """
    Get the real-time quote for a forex pair.
    
    Args:
        symbol (str): The forex pair symbol (e.g., "EURUSD"). [Required]
    
    Returns:
        dict: Real-time quote data for the forex pair.
    """
    return _get(f"v3/quote/{symbol}")

@tool
def get_forex_historical(symbol, from_date=None, to_date=None):
    """
    Get historical price data for a forex pair.
    
    Args:
        symbol (str): The forex pair symbol. [Required]
        from_date (str, optional): Start date for historical data (YYYY-MM-DD).
        to_date (str, optional): End date for historical data (YYYY-MM-DD).
    
    Returns:
        dict: Historical price data for the forex pair.
    """
    request_params = {}
    if from_date:
        request_params["from"] = from_date
    if to_date:
        request_params["to"] = to_date
    return _get(f"v3/historical-price-full/{symbol}", **request_params)

@tool
def get_crypto_list():
    """
    Get a list of available cryptocurrencies.
    
    Returns:
        dict: Available cryptocurrencies.
    """
    return _get("v3/symbol/available-cryptocurrencies")

@tool
def get_crypto_quote(symbol):
    """
    Get the real-time quote for a cryptocurrency.
    
    Args:
        symbol (str): The cryptocurrency symbol (e.g., "BTCUSD"). [Required]
    
    Returns:
        dict: Real-time quote data for the cryptocurrency.
    """
    return _get(f"v3/quote/{symbol}")

@tool
def get_crypto_historical(symbol, from_date=None, to_date=None):
    """
    Get historical price data for a cryptocurrency.
    
    Args:
        symbol (str): The cryptocurrency symbol. [Required]
        from_date (str, optional): Start date for historical data (YYYY-MM-DD).
        to_date (str, optional): End date for historical data (YYYY-MM-DD).
    
    Returns:
        dict: Historical price data for the cryptocurrency.
    """
    request_params = {}
    if from_date:
        request_params["from"] = from_date
    if to_date:
        request_params["to"] = to_date
    return _get(f"v3/historical-price-full/{symbol}", **request_params)

@tool
def get_commodity_list():
    """
    Get a list of available commodities.
    
    Returns:
        dict: Available commodities.
    """
    return _get("v3/quotes/commodity")

@tool
def get_commodity_quote(symbol):
    """
    Get the real-time quote for a commodity.
    
    Args:
        symbol (str): The commodity symbol (e.g., "OIL", "GOLD"). [Required]
    
    Returns:
        dict: Real-time quote data for the commodity.
    """
    return _get(f"v3/quote/{symbol}")

@tool
def get_commodity_historical(symbol, from_date=None, to_date=None):
    """
    Get historical price data for a commodity.
    
    Args:
        symbol (str): The commodity symbol. [Required]
        from_date (str, optional): Start date for historical data (YYYY-MM-DD).
        to_date (str, optional): End date for historical data (YYYY-MM-DD).
    
    Returns:
        dict: Historical price data for the commodity.
    """
    request_params = {}
    if from_date:
        request_params["from"] = from_date
    if to_date:
        request_params["to"] = to_date
    return _get(f"v3/historical-price-full/{symbol}", **request_params)

@tool
def get_etf_info(symbol):
    """
    Get detailed information for an ETF.
    
    Args:
        symbol (str): The ETF symbol. [Required]
    
    Returns:
        dict: ETF information including sector and country weighting.
    """
    return _get("v4/etf-info", symbol=symbol)

@tool
def get_etf_sector_weighting(symbol):
    """
    Get sector weighting for an ETF.
    
    Args:
        symbol (str): The ETF symbol. [Required]
    
    Returns:
        dict: Sector weighting details for the ETF.
    """
    return _get(f"v3/etf-sector-weightings/{symbol}")

@tool
def get_etf_country_weighting(symbol):
    """
    Get country weighting for an ETF.
    
    Args:
        symbol (str): The ETF symbol. [Required]
    
    Returns:
        dict: Country weighting details for the ETF.
    """
    return _get(f"v3/etf-country-weightings/{symbol}")

@tool
def get_etf_stock_exposure(symbol):
    """
    Get stock exposure data for an ETF.
    
    Args:
        symbol (str): The ETF symbol. [Required]
    
    Returns:
        dict: Stock exposure details for the ETF.
    """
    return _get(f"v3/etf-stock-exposure/{symbol}")


@tool
def get_economic_indicator(name):
    """
    Get the value of an economic indicator.
    
    Args:
        name (str): The name of the economic indicator (e.g., "GDP", "Unemployment Rate"). [Required]
    
    Returns:
        dict: Economic indicator data.
    """
    return _get("v4/economic", name=name)

@tool
def get_economic_calendar(from_date=None, to_date=None):
    """
    Get the economic calendar with upcoming events and indicators.
    
    Args:
        from_date (str, optional): Start date for the calendar (YYYY-MM-DD).
        to_date (str, optional): End date for the calendar (YYYY-MM-DD).
    
    Returns:
        dict: Upcoming economic events and indicators.
    """
    request_params = {}
    if from_date:
        request_params["from"] = from_date
    if to_date:
        request_params["to"] = to_date
    return _get("v3/economic_calendar", **request_params)

@tool
def get_market_risk_premium():
    """
    Get the current market risk premium.
    
    Returns:
        dict: Market risk premium data.
    """
    return _get("v4/market_risk_premium")

@tool
def get_ipo_calendar(from_date=None, to_date=None):
    """
    Get the IPO calendar with confirmed upcoming IPOs.
    
    Args:
        from_date (str, optional): Start date for the calendar (YYYY-MM-DD).
        to_date (str, optional): End date for the calendar (YYYY-MM-DD).
    
    Returns:
        dict: Upcoming IPOs.
    """
    request_params = {}
    if from_date:
        request_params["from"] = from_date
    if to_date:
        request_params["to"] = to_date
    return _get("v4/ipo-calendar-confirmed", **request_params)

@tool
def get_stock_news(tickers=None, from_date=None, to_date=None, page=0):
    """
    Get stock-related news for specific tickers within a date range.
    
    Args:
        tickers (list of str, optional): List of stock symbols to filter news by.
        from_date (str, optional): Start date for the news (YYYY-MM-DD).
        to_date (str, optional): End date for the news (YYYY-MM-DD).
        page (int, optional): Page number for pagination. @tool
default is 0.
    
    Returns:
        dict: News articles related to the stocks.
    """
    request_params = {"page": page}
    if tickers:
        if not isinstance(tickers, list):
            raise ValueError("Parameter 'tickers' must be a list of symbols.")
        request_params["tickers"] = ",".join(tickers)
    if from_date:
        request_params["from"] = from_date
    if to_date:
        request_params["to"] = to_date
    return _get("v3/stock_news", **request_params)
