import requests
import os
import json

from fmp_api import *
from utils import *

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Optional, Type, List, Union
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# I usually roll with temp 0, thought some creativity would be nice, and our prompts will be flush with details so
# hallucination is less of a concern.
copilot_llm = ChatOpenAI(api_key=os.getenv("OPEN_AI_API_KEY") ,model="gpt-4o", temperature=1)

tools = [search_company, get_company_profile, get_stock_quote, get_income_statement, get_balance_sheet, 
get_cash_flow, get_market_cap, get_analyst_estimates, get_bulk_quote, get_bulk_income_statements, 
get_bulk_balance_sheets, get_bulk_cash_flows, get_bulk_ratios, get_bulk_key_metrics, 
get_forex_pairs, get_forex_quote, get_forex_historical, get_crypto_list, get_crypto_quote, 
get_crypto_historical, get_commodity_list, get_commodity_quote, get_commodity_historical, 
get_etf_info, get_etf_sector_weighting, get_etf_country_weighting, get_etf_stock_exposure, 
get_economic_indicator, get_economic_calendar, get_market_risk_premium, get_ipo_calendar, 
get_stock_news, get_sec_filings, get_sec_rss_feed, get_earnings_calendar, get_earnings_historical, scrape_url]

# Initialize conversation history
conversation_history = []

# Function to manage history and truncate it to the last 10 messages
def update_conversation_history(user_input, assistant_output):
    # Add new user-assistant pair to the conversation history
    conversation_history.append({"human": user_input, "assistant": assistant_output})
    
    # If history exceeds 10 pairs, remove the oldest one
    if len(conversation_history) > 10:
        conversation_history.pop(0)

# Start a conversation loop with the copilot
def run_conversation():
    print("Welcome to the Stock Trader Copilot! Type 'exit' to end the conversation.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending conversation. Goodbye!")
            break

        # Prepare context with the last 10 message pairs
        context_messages = []
        for pair in conversation_history:
            context_messages.append(("human", pair['human']))
            context_messages.append(("assistant", pair['assistant']))
        
        # Add the current user input to the context
        context_messages.append(("human", user_input))
        
        # Create a dynamic prompt for the current conversation
        dynamic_prompt = ChatPromptTemplate.from_messages(
            #Providing today's date such that the LLM doesn't think its sometime in 2023, when it was trained
            [("system", f"You are a stock trader co-pilot. Give useful answers to the trader's questions. Today's date is: {get_todays_date()}")] +
            context_messages +
            [("placeholder", "{agent_scratchpad}")]
        )

        # Create the agent with updated context
        agent = create_tool_calling_agent(copilot_llm, tools, dynamic_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        # Pass the user input to the agent executor
        result = agent_executor.invoke({"input": user_input})
        assistant_output = result['output']
        
        # Display the copilot's response
        print("Copilot: ", assistant_output)

        # Update the conversation history
        update_conversation_history(user_input, assistant_output)

# Run the conversation loop
run_conversation()