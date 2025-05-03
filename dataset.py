import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import streamlit as st



import wikipedia





wikipedia.set_lang("en")

stock_symbol = "TATASTEEL.NS"
stocks_start_date = datetime.datetime(2023, 1, 1)
today = datetime.datetime.today()

#assets =['AAPL','AMZN','GOOG','NFLX']
stocksstartdate='2023-08-28'

def get_stock_data(stock_input,start_date,end_date):
  df[stock_input] = yf.download(stock_input, start=start_date, end=end_date)['Adj Close']      #fakta adj close
  return df


def closely(stock_input):                                                     # low deto
    df=yf.download(stock_input, start=stocksstartdate, end=today)['Low']
    return df

def complete_stock_data(stock_input,start_date,end_date):                                          #full complete deto
    df = yf.download(stock_input, start=start_date, end=end_date)
    return df

def High_data(vol_input,start_date,end_date):                                          #full complete deto
    ab[vol_input] = yf.download(vol_input, start=start_date, end=end_date)['High']
    return ab

def Low_data(stock_input,start_date,end_date):                                          #full complete deto
    df= yf.download(stock_input, start=start_date, end=end_date)['Volume']
    return ab


def full_exceptVolume(stock_input,start_date,end_date):                       # volume nai det bas
    df = yf.download(stock_input, start=start_date, end=end_date)
    df = df.drop(columns=['Volume'])
    return df


low = pd.DataFrame()
ab=pd.DataFrame()
df = pd.DataFrame()
