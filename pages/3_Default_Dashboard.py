import pandas as pd
import streamlit as st
from dataset import full_exceptVolume, complete_stock_data, get_stock_data
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(page_title="Single Equity analysis", page_icon=":bar_chart:", layout="wide")

# st.markdown(
#     """
# <style>
# .sidebar .sidebar-content {
#     background-image: linear-gradient(#2e7bcf,#2e7bcf);
#     color: white;
# }
# </style>
# """,
#     unsafe_allow_html=True,
# )

bg1="https://b2316719.smushcdn.com/2316719/wp-content/uploads/2022/03/bg_06-768x384.jpg?lossy=1&strip=1&webp=1"
bg2="https://img.freepik.com/free-photo/abstract-luxury-gradient-blue-background-smooth-dark-blue-with-black-vignette-studio-banner_1258-52393.jpg?w=1380&t=st=1699467722~exp=1699468322~hmac=c04d81ce6221678b8377e6b4850bbb25a939a155a3973902fafbd186fba9de86"
bg="https://wallpapers.com/images/high/stock-market-simple-representation-mqustwxvlchtj32h.webp"
bg3="https://cdn.pixabay.com/photo/2015/10/15/21/37/texture-990104_1280.jpg"
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1601333924581-7b48591a926c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# def full(stock_input):
#     df = yf.download(stock_input, start=stocksstartdate, end=today)
#     return  df
# lol = full('tcs.ns')
# st.write(lol)

emoj=':globe_with_meridians:'
emoj2=":chart_with_upwards_trend:"
emoj3=':chart_with_downwards_trend:'
file_emoj4=':clipboard:'
emojis= ''':alarm_clock:
1743	⏱️	:stopwatch:
1744	⏲️	:timer_clock:
1745	⏳	:hourglass_flowing_sand:'''

TL, M, TR, TMR = st.columns(4)
col1, col2 = st.columns([2, 1])


dash_width=700
full_width=900
##see below for this

width= st.sidebar.selectbox('Select DashBoard Layout:', ["Dash-View", "Full-View"])
if width=="Dash-View":
 width1=dash_width
elif width=="Full-View":
 width1=full_width


if 'stock_input' not in st.session_state:
    st.session_state.stock_input = None
if 'start_date' not in st.session_state:
    st.session_state.start_date = None
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None


selected_option = st.sidebar.selectbox("Select Stock Type:", ["Indian Stocks", "International stocks"])
stock_input= st.sidebar.text_input('Enter stock Name')
if (selected_option=="Indian Stocks"):
  NorB= st.sidebar.radio("Choose Your exchange:", ["BSE", "NSE"])
  if (NorB=="NSE"):
   stock_input=stock_input+'.ns'
   # st.write(stock_input)
  elif(NorB=="BSE"):
   stock_input = stock_input + '.bo'
   # st.write(stock_input)
start_date=st.sidebar.date_input(":spiral_calendar_pad: Start Date:")
end_date=st.sidebar.date_input(':watch: End Date:')


def display_charts(stock_input, start_date , selected_option):  
  st.write(stock_input)
  full_data= full_exceptVolume(stock_input,start_date,end_date)

  
  full_data_flat = full_data.copy()
  if isinstance(full_data.columns, pd.MultiIndex):
      full_data_flat.columns = ['_'.join(col).strip() for col in full_data.columns.values]


  complete_data = complete_stock_data(stock_input,start_date,end_date)
  st.write(complete_data)
  #Adj_close_data = get_stock_data(stock_input,start_date,end_date)
  volume_data = complete_data['Volume']
                                                      # datbase view ahe
  with col1:  # Line Chart
      line = px.line(full_data_flat, title='Single stock visualizer')
      line.update_layout(
          height=350,
          width=full_width,  # Use full width for line chart
      )
      st.plotly_chart(line)

  
        

  with col2:  # Donut Chart
      # Ensure we get scalar values
    price_change = (complete_data['Close'] - complete_data['Open']).mean()
    normalized_volume = (complete_data['Volume'] - complete_data['Volume'].min()) / (
        complete_data['Volume'].max() - complete_data['Volume'].min())

    # Convert them into pure numbers (floats)
    price_change_value = price_change.item()  # Convert to scalar value
    normalized_volume_value = normalized_volume.mean().item()  # Convert to scalar value

    # Display the values for debugging
    # st.write(f"Price Change: {price_change_value}")
    # st.write(f"Normalized Volume: {normalized_volume_value}")

    # Create the donut data
    donut_data = pd.DataFrame({
        'Attribute': ['Price Change', 'Volume'],
        'Value': [price_change_value, normalized_volume_value]
    })

  
    # Create and display the pie chart
    fig = px.pie(donut_data, names='Attribute', values='Value', hole=0.5)
    fig.update_layout(
        title='Price Change vs. Volume (Mean)',
        height=350,
        width=full_width,
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        plot_bgcolor='rgba(0, 0, 0, 0)'
    )
    

    st.plotly_chart(fig)

  #   # Display the Donut Chart in Streamlit

  with TL: 
    # Calculate the average trading volume as a single numeric value (float)
    avg_volume = complete_data['Volume'].values.mean()

  #   # Debug: Print the value to check if it's a scalar
  #   st.write(f"Average Volume: {avg_volume}")

    # # Create the gauge chart with the extracted avg_volume as a scalar value
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_volume,  # Ensure this is a scalar value (float)
        title={'text': "Average Trading Volume"},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))

    # Update the layout of the gauge chart
    fig.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
        width=300,
        height=270
    )

    # Display the gauge chart in Streamlit
    st.plotly_chart(fig)
                                                                    #gauge chart
  
  with M:

    st.write(complete_data.columns)
  #   if not Adj_close_data.empty:
  #     returns = Adj_close_data.values.pct_change().dropna()
  #   else:
  #     st.warning("No data available for percentage change calculation")
  #     returns = pd.Series()
  #   #returns = full_data['Adj Close'].pct_change().dropna()
  #   volatility = returns.std()
  #   fig = go.Figure(go.Indicator(
  #    mode="gauge+number",
  #    value=volatility,
  #    title={'text': "volatility"},
  #    domain={'x': [0, 1], 'y': [0, 1]}
  #   ))
  #   fig.update_layout(
  #   paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
  #   plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
  #   )
  #   fig.update_layout(width=300, height=270)
  #   # Display the gauge chart in Streamlit
  #   st.plotly_chart(fig)

  with TMR:                                #  indicator
    fig = go.Figure()
    maximum = full_data['High'].values.max()
    minimum= full_data['Low'].values.min()
    fig.add_trace(go.Indicator(
    mode="number+delta",
    value=maximum,
    title={
      "text": stock_input+ ":<br><span style='font-size:0.8em;color:gray'>MAX returns</span><br><span style='font-size:0.8em;color:gray'>High-Low</span>"},
    delta={'reference': minimum, 'relative': True},
    domain={'x': [0, 1], 'y': [0, 1]}))
    fig.update_layout(height=270,width=300,
    paper_bgcolor = 'rgba(0, 0, 0, 0)',  # Transparent background
    plot_bgcolor = 'rgba(0, 0, 0, 0)',
    )
    st.write(fig, align='center')

  with TR:
    volume_data = complete_data['Volume']
    line = px.line(volume_data, title='Stock volume Visualizer')  # line wala
    line.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
    )
    line.update_layout(width=300, height=270)
    st.plotly_chart(line)



if (st.session_state.stock_input is None or 
    st.session_state.start_date is None or 
    st.session_state.selected_option is None):
    display_charts("amzn", "2024-09-02", "International stocks")  # Default to Amazon
else:
    display_charts(st.session_state.stock_input, st.session_state.start_date, st.session_state.selected_option)

# if stock_input==None and start_date==None and selected_option==None:
#    display_charts("amzn", "2024-09-02" , "International stocks") 
#    #display_charts(stock_input, start_date, selected_option)
# else:
#    display_charts(stock_input, start_date, selected_option)   
  

