# Stock Trader Copilot

The **Stock Trader Copilot** is an interactive assistant designed to help traders and analysts quickly retrieve financial data, answer stock-related questions, and perform various financial tasks. It integrates with multiple financial tools and data sources to provide comprehensive market insights in real-time using OpenAI's language models.

## Features

- **Stock data retrieval**: Get quotes, company profiles, balance sheets, cash flows, and other financial metrics for stocks, ETFs, forex, commodities, and cryptocurrencies.
- **Conversation-based interaction**: Chat with the co-pilot to get answers to trading-related questions in a human-like manner.
- **Tool integration**: Uses a wide range of tools to fetch data such as stock quotes, analyst estimates, economic indicators, etc.
- **History tracking**: Keeps a running log of up to the last 10 user queries and assistant responses for more contextualized conversations.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Environment Variables](#environment-variables)
5. [Available Tools](#available-tools)
6. [Contributing](#contributing)
7. [License](#license)

## Requirements

- Python 3.8+
- An OpenAI API key for accessing GPT models
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/VictorHadziristic/Finchat
    cd stock-trader-copilot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3. Set up environment variables (see [Environment Variables](#environment-variables)).

## Usage

To start the Stock Trader Copilot:

1. Ensure that your OpenAI API key and other environment variables are set.
2. Run the `run_conversation()` function in the script:
    ```bash
    python main.py
    ```

The co-pilot will guide you through the conversation, where you can ask various questions about stock data and other market-related topics.

### Example:

```
Welcome to the Stock Trader Copilot! Type 'exit' to end the conversation.

You: Get the latest stock quote for AAPL.
Copilot: [AAPL quote details]
```

## Environment Variables

Set the following environment variables:

- `OPEN_AI_API_KEY`: Your OpenAI API key for accessing GPT-4o.
- `FMP_API_KEY`: Your FMP API key.

You can set these in your terminal session or create a `.env` file.

## Available Tools

The co-pilot is integrated with several tools to fetch financial data. Here is a list of available tools:

- `search_company`: Searches for companies.
- `get_company_profile`: Fetches a company profile.
- `get_stock_quote`: Gets the current stock quote.
- `get_income_statement`: Retrieves the income statement for a company.
- `get_balance_sheet`: Retrieves the balance sheet for a company.
- `get_cash_flow`: Retrieves the cash flow for a company.
- `get_market_cap`: Fetches the market capitalization of a company.
- And many more...

See the `fmp_api.py` and `utils.py` for additional tools and custom utility functions.