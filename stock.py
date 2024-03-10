import yfinance as yf
import streamlit as st
import datetime

st.header('STOCK PRICING APP')
stock=st.text_input('Enter the stock code:','MSFT')
data = yf.Ticker(stock)

st.write('Currently Analysing:', stock)

start_date=st.date_input('Enter the start date',datetime.date(2019,1,1))
end_date=st.date_input('Enter the end date',datetime.date(2019,1,1))
hist = data.history(period='1d', start=start_date, end=end_date)
st.write(hist)

st.subheader('Trend in closing price')
st.line_chart(hist['Close'])