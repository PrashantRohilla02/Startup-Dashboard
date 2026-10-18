# Startup Funding Analysis Dashboard

A Streamlit dashboard for exploring startup funding and investor activity in the
included dataset. It provides summary metrics, interactive charts, and details
about selected startups and investors. Startup summaries can also be requested
from Google Gemini.

## Features

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

## Setup

Open a terminal in the project directory and create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell prevents activating the environment, you can invoke its Python
directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

In VS Code, select the `.venv` Python interpreter for this workspace so the
editor and the application use the same installed packages.

## Configure Gemini

Create a `.env` file in the project root and add your API key:

```dotenv
GOOGLE_API_KEY=your_google_gemini_api_key
```

The application loads this file when requesting a startup summary. Keep the
key private; do not commit `.env` to version control. You can obtain a key from
[Google AI Studio](https://aistudio.google.com/app/apikey).

## Run the dashboard

From the project root, start Streamlit:

```powershell
python -m streamlit run startup.py
```

Open the local URL printed by Streamlit (usually
`http://localhost:8501`). Use the sidebar to switch among **Overall**,
**About Startup**, and **About Investors**.

## Dataset

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
├── Data_fetch.py
├── startup.py
├── requirements.txt
└── Dataset/
    ├── startup_funding.csv
    ├── startup_funding_cleaned.csv
    └── startup_funding_cleaned2.csv
```

- [`startup.py`](startup.py) builds the Streamlit interface and connects the
  sidebar selections to the analysis functions.
- [`Data_fetch.py`](Data_fetch.py) loads and processes the CSV, computes
  summary data, renders visualizations, and requests Gemini summaries.
- [`requirements.txt`](requirements.txt) lists the Python dependencies.
