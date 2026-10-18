# Startup Funding Analysis Dashboard

A Streamlit-powered interactive dashboard designed to explore startup funding trends and investor activity. It offers comprehensive summary metrics, interactive visualizations, and detailed profiles for specific startups and investors, enhanced with AI-generated insights via Google Gemini.

## Core Features

- **Overall analysis:** total funding, average funding per startup, largest
  startup funding total, yearly trends, and monthly trends for a selected year.
- **Top lists:** leading investors, funded startups, and yearly top funding
  rounds.
- **Startup lookup:** view industry and sub-industry information, city, and an
  AI-generated introduction.
- **Investor lookup:** view recent investments, the largest investment, sector
  distribution, and yearly investment totals.

## Requirements

- Python installed on your machine.
- Packages listed in [`requirements.txt`](requirements.txt).
- A Google Gemini API key to use AI-generated startup summaries. The rest of
  the dashboard does not require this feature.

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

The application loads this file when requesting a startup summary. Keep the
key private; do not commit `.env` to version control. You can obtain a key from
[Google AI Studio](https://aistudio.google.com/app/apikey).

## Running the Dashboard

Launch the Streamlit application from the project root:

```powershell
python -m streamlit run startup.py
```

Navigate to the local URL provided in the terminal (typically `http://localhost:8501`). Use the sidebar menu to toggle between the **Overall**, **About Startup**, and **About Investors** views.

## Dataset Requirements

The application reads `Dataset/startup_funding_cleaned2.csv` when
[`Data_fetch.py`](Data_fetch.py) is imported. Keep this file at that path. The
analysis uses columns including:

- `Startup Name`
- `Date`
- `Amount in USD`
- `Investors Name`
- `Industry Vertical`
- `SubVertical`
- `City`
- `Investement Type`

The dashboard drops rows containing missing values and parses `Date` to derive
year and month values. Ensure the CSV's column names match the names above.

## Project files

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
