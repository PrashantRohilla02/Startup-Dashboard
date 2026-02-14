import os
import pandas as pd
import numpy as np
import streamlit as st 
import matplotlib.pyplot as plt
import plotly.express as px
import requests

startup = pd.read_csv('Dataset\startup_funding_cleaned2.csv')
startup.dropna(inplace=True)


startups_grp = startup.groupby("Startup Name")
startup["Date"] = pd.to_datetime(startup["Date"],errors="coerce")
startup["year"] = startup["Date"].dt.year
startup["month"] = startup["Date"].dt.month



# all Startups
All_Startup = startup["Startup Name"].dropna().unique().tolist()

# all investors
All_investors = (startup["Investors Name"].str.split(",").dropna()).sum()

# to format number
def format_number(num):
    if num >= 1e12:
        return f"{round(num/1e12, 1)} Trillion"
    elif num >= 1e9:
        return f"{round(num/1e9, 1)} Billion"
    elif num >= 1e6:
        return f"{round(num/1e6, 1)} Million"
    elif num >= 1e3:
        return f"{round(num/1e3, 1)} Thousand"
    else:
        return str(num)

# for overall Analysis
def overall_money():
    total = startup["Amount in USD"].sum()
    short = format_number(total)
    st.metric("Total amount Invested","$" +short)

def max_amount():
    total = startup.groupby("Startup Name")["Amount in USD"].sum().sort_values(ascending=False).head(1).values[0]
    short = format_number(total)
    st.metric("Max Amount","$" +short)

def avg_amount():
    total = startup.groupby("Startup Name")["Amount in USD"].sum().mean()
    short = format_number(total)
    st.metric("Avg Amount","$" +short)

def yoy_invested():
    yoy = startup.groupby("year")["Amount in USD"].sum().reset_index()
    fig = px.bar(yoy,x='year',y='Amount in USD')
    # fig, ax = plt.subplots()
    # ax.bar(yoy.index,yoy.values)
    # ax.set_title("YOY - Investement")

    # st.pyplot(fig)
    st.plotly_chart(fig)


def top_investors():
    st.subheader("Top Investors")
    top = startup.groupby("Investors Name")["Amount in USD"].sum().sort_values(ascending=False).head(10).reset_index()
    st.dataframe(top.head(5))

def top_startups():
    st.subheader("Top Startups by Funding")
    top_stat = startup.groupby("Startup Name")["Amount in USD"].sum().sort_values(ascending=False).head(10).reset_index()
    st.dataframe(top_stat.head(5))

def MoM_investement():
    years = startup["year"].unique().tolist()
    year = st.selectbox("Select Year",years,placeholder="select year")
    stt = startup.groupby(["year","month"])["Amount in USD"].sum().reset_index()

    stt = stt[stt["year"] == year]
    fig = px.bar(stt,x="month",y="Amount in USD",width=100,height=382)
    # fig, ax = plt.subplots()
    # ax.bar(stt["month"],stt["Amount in USD"])
    # ax.set_title("YOY - Investement")

    # st.pyplot(fig)
    st.plotly_chart(fig)


# fetching the information of each comapnies
def comp_info(startup_name):
    startup_details = startup[startup['Startup Name'] == startup_name]
    st.dataframe(startup_details[["Industry Vertical","SubVertical"]])

def location(startup_name):
    startup_loc = startup[startup['Startup Name'] == startup_name]
    st_city =startup_loc["City"].value_counts()
    for value in st_city.index:
         st.write(value)

# api Calling to get information of startup
def Info(startup_name):
    from dotenv import load_dotenv
    from google import genai
    
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        return "GEMINI_API_KEY not found in environment. Please check your .env file."

    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=f"tell about {startup_name} its founder and anyhting as its introduction"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# year wise top startups
def top_performer():
    year = st.selectbox("Year Top Performer", startup["year"].unique().tolist(),placeholder="select year ")
    top_performer = startup[startup["year"] == year]
    tp = top_performer.sort_values(by="Amount in USD",ascending=False).head(5)

    st.dataframe(tp[["Startup Name","Industry Vertical","Investement Type","Amount in USD"]])


# to fetch investor details
def load_investor_data(investor_name):
    st.subheader("Recent Investements")
    Recent_investements = startup[startup["Investors Name"].str.contains(investor_name)]
    Recent_investements = Recent_investements[["Date","Industry Vertical","City","Investement Type","Amount in USD"]]
    st.dataframe(Recent_investements.head(5))

# to fetch biggest investement of each investor
def biggest_investement(investor_name):
    st.subheader("Biggest Investement")
    Biggest = startup[startup["Investors Name"].str.contains(investor_name)].groupby("Startup Name")["Amount in USD"].sum().sort_values(ascending=False)
    top_one = Biggest.index[0]
    most_invested = startup[startup["Startup Name"] == top_one]
    top = Biggest.head(5) # to reduce conjustion it shows only five values
    st.dataframe(most_invested[["Date","Startup Name","Industry Vertical","Investement Type","Amount in USD"]].head(1))

    # with graph also
    col,col2 = st.columns(2)
    with col:
        st.subheader("Graph of investement")
        fig, ax = plt.subplots()
        ax.bar(top.index,top.values)
        st.pyplot(fig)
        
    with col2:
        st.subheader("Most Amount Invested in each Sector")
        invested_verticle = startup[startup["Investors Name"].str.contains(investor_name)].groupby("Industry Vertical")["Amount in USD"].sum().reset_index()
        fig = px.pie(invested_verticle,values="Amount in USD",names="Industry Vertical")
        # fig, ax = plt.subplots()
        # ax.pie(invested_verticle,labels=invested_verticle.index)

        # st.pyplot(fig)
        st.plotly_chart(fig)

startup.info()

def yoy_investements(investor_name):
        col_a,col_b = st.columns(2)
        with col_a:
            st.subheader("YoY Investment")
            yoy = startup[startup["Investors Name"].str.contains(investor_name)].groupby("year")["Amount in USD"].sum().reset_index()
            
            fig = px.bar(yoy,x="year",y="Amount in USD")
            st.plotly_chart(fig)
            


 