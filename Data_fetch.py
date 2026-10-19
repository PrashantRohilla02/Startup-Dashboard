import os
import pandas as pd
import numpy as np
import streamlit as st 
try:
    import matplotlib.pyplot as plt
    _MATPLOTLIB_AVAILABLE = True
except Exception:
    _MATPLOTLIB_AVAILABLE = False
import plotly.express as px
import requests
from langchain_google_genai import ChatGoogleGenerativeAI


startup = pd.read_csv('Dataset/startup_funding_cleaned2.csv')
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
    fig = px.bar(yoy,x='year',y='Amount in USD',color="Amount in USD",color_continuous_scale="magenta")
    # fig, ax = plt.subplots()
    # ax.bar(yoy.index,yoy.values)
    # ax.set_title("YOY - Investement")

    # st.pyplot(fig)
    st.plotly_chart(fig)


def top_investors():
    st.subheader("Top 5 Investors")
    top = startup.groupby("Investors Name")["Amount in USD"].sum().sort_values(ascending=False).head(10).reset_index()
    st.dataframe(top,
        column_config={
            "Investors Name": "Investor",
            "Amount in USD": st.column_config.ProgressColumn(
                "Funding Amount (USD)",
                format="%d",
                min_value=0,
                max_value=int(top["Amount in USD"].head(5).max()),
            ),
        },
        hide_index=True,
        width="stretch")

def top_startups():
    st.subheader("Top 5 Startups which got highest Funding")
    top_stat = startup.groupby("Startup Name")["Amount in USD"].sum().sort_values(ascending=False).head(10).reset_index()
    st.dataframe(top_stat,
        column_config={
            "Startup Name": "Startup",
            "Amount in USD": st.column_config.ProgressColumn(
                "Funding Received (USD)",
                format="$%d",
                min_value=0,
                max_value=int(top_stat["Amount in USD"].max()),
            ),
        },
        hide_index=True,
        use_container_width=True)

def MoM_investement():
    years = startup["year"].unique().tolist()
    year = st.selectbox("Select Year",years,placeholder="select year")
    stt = startup.groupby(["year","month"])["Amount in USD"].sum().reset_index()

    stt = stt[stt["year"] == year]
    fig = px.bar(stt,x="month",y="Amount in USD",width=100,height=382,color="Amount in USD",color_continuous_scale="Viridis")
    # fig, ax = plt.subplots()
    # ax.bar(stt["month"],stt["Amount in USD"])
    # ax.set_title("YOY - Investement")

    # st.pyplot(fig)
    st.plotly_chart(fig)


# fetching the information of each comapnies
def comp_info(startup_name):
    df = startup[startup['Startup Name'] == startup_name]
    
    if df.empty:
        st.info("No startup details available.")
        return

    vertical = ", ".join(df["Industry Vertical"].dropna().unique()) or "N/A"
    subvertical = ", ".join(df["SubVertical"].dropna().unique()) or "N/A"

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Industry Vertical", value=vertical)
    with col2:
        st.metric(label="Sub-Vertical", value=subvertical)

def location(startup_name):
    df = startup[startup['Startup Name'] == startup_name]
    cities = df["City"].dropna().unique().tolist()
    
    if not cities:
        st.info("Location details unavailable.")
        return

    st.markdown("**Company Location(s):**")
    # Native pill badges
    st.pills(label="Locations", options=cities, selection_mode="multi", default=cities, disabled=True)

# api Calling to get information of startup
def Info(startup_name):
    from dotenv import load_dotenv
    load_dotenv()
    try:
        response = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview"
            
        )
        return response.invoke(f"tell about {startup_name} its founder and anyhting as its introduction").content[0]["text"]
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
    st.subheader("⏱️ Recent Investments")
    
    recent = startup[startup["Investors Name"].str.contains(investor_name, case=False, na=False)]
    
    if recent.empty:
        st.info("No recent investments found.")
        return

    cols = ["Date", "Industry Vertical", "City", "Investement Type", "Amount in USD"]
    recent_deals = recent[cols].head(5)

    st.dataframe(
        recent_deals,
        column_config={
            "Date": st.column_config.DateColumn("Date"),
            "Industry Vertical": st.column_config.TextColumn("Sector / Vertical"),
            "City": st.column_config.TextColumn("Location"),
            "Investement Type": st.column_config.TextColumn("Round Type"),
            "Amount in USD": st.column_config.NumberColumn(
                "Amount",
                format="$%d"
            ),
        },
        hide_index=True,
        use_container_width=True
    )

# to fetch biggest investement of each investor
def biggest_investment(investor_name):

   

    # Safe filtering with case-insensitive search and null checks
    investor_df = startup[startup["Investors Name"].str.contains(investor_name, case=False, na=False)]

    if investor_df.empty:
        st.warning(f"No investment record found for '{investor_name}'.")
        return

    # 1. TOP INVESTMENT HIGHLIGHT (Replaces single-row DataFrame with Metric Cards)
    biggest = investor_df.groupby("Startup Name")["Amount in USD"].sum().sort_values(ascending=False)
    top_one_name = biggest.index[0]
    top_deal = investor_df[investor_df["Startup Name"] == top_one_name].iloc[0]

    st.markdown("#### 🏆 Single Largest Investment Deal")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(label="Startup Name", value=str(top_deal["Startup Name"]))
    with kpi2:
        st.metric(label="Funding Amount", value=format_number(top_deal["Amount in USD"]))
    with kpi3:
        st.metric(label="Industry Vertical", value=str(top_deal.get("Industry Vertical", "N/A")))
    with kpi4:
        st.metric(label="Investment Type", value=str(top_deal.get("Investment Type", "N/A")))

    st.markdown("---")

    # 2. VISUAL CHARTS GRID
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 5 Investments")
        top_5 = biggest.head(5).reset_index()

        # Horizontal bar chart prevents label overlaps on long startup names
        fig_bar = px.bar(
            top_5,
            x="Amount in USD",
            y="Startup Name",
            orientation="h",
            text=top_5["Amount in USD"].apply(format_number),
            color="Amount in USD",
            color_continuous_scale="Blues"
        )
        fig_bar.update_traces(textposition="outside")
        fig_bar.update_layout(
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            xaxis_title="Investment ($)",
            yaxis_title="",
            height=320,
            margin=dict(l=0, r=10, t=10, b=10)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("Sector Allocation")
        invested_vertical = investor_df.groupby("Industry Vertical")["Amount in USD"].sum().reset_index()

        # Modern Donut chart instead of default pie chart
        fig_donut = px.pie(
            invested_vertical,
            values="Amount in USD",
            names="Industry Vertical",
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_donut.update_traces(textinfo="percent+label")
        fig_donut.update_layout(
            showlegend=False,
            height=320,
            margin=dict(l=0, r=0, t=10, b=10)
        )
        st.plotly_chart(fig_donut, use_container_width=True)
startup.info()

def yoy_investements(investor_name):
        col_a,col_b = st.columns(2)
        with col_a:
            st.subheader("YoY Investment")
            yoy = startup[startup["Investors Name"].str.contains(investor_name)].groupby("year")["Amount in USD"].sum().reset_index()
            
            fig = px.bar(yoy,x="year",y="Amount in USD",color="Amount in USD",color_continuous_scale="magenta")
            st.plotly_chart(fig)
            


 