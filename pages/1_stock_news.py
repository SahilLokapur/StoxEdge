import streamlit as st
import yfinance as yf
import datetime

# Title of the Streamlit app
st.title('Stock Data from Yahoo Finance')

# Input box for stock ticker symbol
ticker = st.text_input("Enter Stock Ticker Symbol", "AAPL")

# Select start and end date for the short period
start_date = st.date_input("Start Date", datetime.date(2023, 1, 1))
end_date = st.date_input("End Date", datetime.date(2023, 12, 31))

# Fetch the stock data
if ticker:
    try:
        # Download stock data for the specified date range
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        # Check if the stock data was successfully fetched
        if stock_data.empty:
            st.error(f"No data found for {ticker} in the given date range.")
        else:
            st.write(f"Showing stock data for {ticker} from {start_date} to {end_date}")
            st.dataframe(stock_data)  # Show the stock data in a table
            
            # Display Adjusted Close data if it exists
            if 'Adj Close' in stock_data.columns:
                st.write(f"Adjusted Close Data for {ticker}:")
                st.line_chart(stock_data['Adj Close'])  # Line chart for adjusted close
            else:
                st.warning("Adjusted Close data is not available for this ticker in the given period.")
    
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
