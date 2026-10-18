# Startup Funding Analysis Dashboard

A Streamlit-powered interactive dashboard designed to explore startup funding trends and investor activity. It offers comprehensive summary metrics, interactive visualizations, and detailed profiles for specific startups and investors, enhanced with AI-generated insights via Google Gemini.

## Core Features

- **Market Overview:** Analyze total funding, average funding per startup, record-high funding rounds, and track trends across years and specific months.
- **Top Leaderboards:** Identify the most active investors, highest-funded startups, and the top funding rounds annually.
- **Startup Intelligence:** View a startup's industry vertical, sub-vertical, location, and an AI-generated introductory summary.
- **Investor Portfolios:** Track an investor's recent investments, their largest single investment, sector distribution, and year-over-year investment totals.

## Prerequisites

- Python installed on your machine.
- Dependencies listed in [`requirements.txt`](requirements.txt).
- **Google Gemini API Key:** Required only for the AI-generated startup summaries. All other dashboard features function normally without it.

## Installation & Setup

Open a terminal in the project root directory and create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

> **Note for Windows Users:** If PowerShell execution policies prevent activation, you can invoke the virtual environment's Python executable directly to install packages:
> `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

If you are using **VS Code**, select the `.venv` Python interpreter for this workspace so the editor correctly resolves your installed dependencies.

## Configuration

To enable AI-generated startup summaries, create a `.env` file in the root directory and add your Google Gemini API key (obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey)):

```dotenv
GOOGLE_API_KEY=your_google_gemini_api_key
```

_Keep this key secure. Ensure `.env` is not committed to version control._

## Running the Dashboard

Launch the Streamlit application from the project root:

```powershell
python -m streamlit run startup.py
```

Navigate to the local URL provided in the terminal (typically `http://localhost:8501`). Use the sidebar menu to toggle between the **Overall**, **About Startup**, and **About Investors** views.

## Dataset Requirements

The application automatically loads the dataset from `Dataset/startup_funding_cleaned2.csv` upon importing [`Data_fetch.py`](Data_fetch.py). The script drops rows with missing values and parses the `Date` column to extract yearly and monthly data.

Ensure your CSV file remains at this exact path and includes the following column headers:

- `Startup Name`
- `Date`
- `Amount in USD`
- `Investors Name`
- `Industry Vertical`
- `SubVertical`
- `City`
- `Investement Type`

## Project Structure

```text
.
├── Data_fetch.py       # Handles CSV data processing, aggregations, visualizations, and Gemini API requests
├── startup.py          # Main Streamlit interface and sidebar routing logic
├── requirements.txt    # Project dependencies
└── Dataset/
    ├── startup_funding.csv
    ├── startup_funding_cleaned.csv
    └── startup_funding_cleaned2.csv  # Primary dataset used by the application
```
