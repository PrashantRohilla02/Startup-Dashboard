import streamlit as st
import Data_fetch
import plotly.express as px

st.set_page_config(layout="wide",page_title="Startup Analysis")
st.sidebar.title("Startup Analysis")
option = st.sidebar.selectbox("What analysis do you want",["Overall","About Startup","About Investors"])

if option == "Overall":
        st.header("Overall Analysis")
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            Data_fetch.overall_money()
        with col2:
            Data_fetch.max_amount()
        with col3:
            Data_fetch.avg_amount()
       
        col5,col6 = st.columns(2)
        with col5:
            st.subheader("YoY invested in Startups")
            st.write("")
            Data_fetch.yoy_invested()
        with col6:
            st.subheader("MoM investement in a year")
            Data_fetch.MoM_investement()

        Data_fetch.top_investors()
        Data_fetch.top_startups()
        Data_fetch.top_performer()

elif option == "About Startup":
    startup_name = st.sidebar.selectbox(option,Data_fetch.All_Startup,placeholder="Select Startup Name")
    st.title(startup_name)
    # st.write(Data_fetch.comp_info(startup_name))
    btn1 = st.sidebar.button("Find Startup Details")
  
    if btn1:
        st.write(Data_fetch.Info(startup_name))
        st.subheader("Vertical and Subvertical")
        Data_fetch.comp_info(startup_name)
        st.subheader("Comapany Location")
        Data_fetch.location(startup_name)

elif option == "About Investors":
    investor_name = st.sidebar.selectbox(option,Data_fetch.All_investors,placeholder="Select Investor name")
    st.title(investor_name)
    btn2 = st.sidebar.button("Find Investor details")
    

    if btn2:
       Data_fetch.load_investor_data(investor_name)
       Data_fetch.biggest_investement(investor_name)
       Data_fetch.yoy_investements(investor_name)
       
