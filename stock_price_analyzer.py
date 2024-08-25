import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import date
import datetime

st.write(
    """
    # Stock Price Analyzer

    Shown are the stock prices of Apple.
    """
)

ticker_symbol = st.text_input(
                              "Enter the Symbol",
                              "AAPL",
                              key="placeholder",)
# ticker_symbol = "AAPL"

col1, col2 = st.columns(2)

# Start date analysis
with col1:
    start_date = st.date_input("Input Starting Date",
                    datetime.date(2019,1,1))

# End date analysis
with col2:
    end_date = st.date_input("Input End Date",
                    value=date.today())


ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d",
                                start=f"{start_date}",
                                end=f"{end_date}")

st.write(f"""
{ticker_symbol}'s EOD Prices""")

st.dataframe(ticker_df)

# Showcasing Chart

st.write("""
        ## Daily Closing Price Chart
""")
st.line_chart(ticker_df.Close)


st.write("""
        ## Volume of Shares traded each day
""")
st.line_chart(ticker_df.Volume)