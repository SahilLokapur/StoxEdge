import streamlit as st
import streamlit.components.v1 as components
import variables

st.set_page_config(page_title="Login Page", page_icon=":bar_chart:", layout="centered")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapers.com/images/featured-full/stock-market-pd5zksxr07t7a4xu.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

another_img="https://w0.peakpx.com/wallpaper/139/711/HD-wallpaper-financial-stock-market-graph-on-stock-market-investment-trading-bullish-point-bearish-point-trend-of-graph-for-business-idea-and-all-art-work-design-vector-illustration-5299428-vector-art-at-vecteezy.jpg"
sec_img="https://wallpapers.com/images/high/stock-market-simple-representation-mqustwxvlchtj32h.webp"


my_js=  f'''
alert('welcome Admin, your authorization was successful');

'''
#st.write("hello mr")
abab = 33

st.title(' :violet[StocxEdge] : optimize your investments and test them')
username=st.text_input('Username')
password=st.text_input('[Password]', type='password')
submit = st.button('Submit')
if (submit==True):
    if(username=='admin')and(password=='admin'):
        st.write('authentificatin successful')
        components.html(f"""
        <body>
        
        </body>
        <script>
        {my_js}
        </script>
        
        """)
        variables.login_switch='ok'





    else:
        st.write('sorry invalid password try again')
        variables.login_switch='not_ok'




# Custom CSS to set the background image (with a relative path)
background_css = """
<style>
body {
    background-image: url('stock1.jpg');
    background-size: cover;
}
</style>
"""

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)


