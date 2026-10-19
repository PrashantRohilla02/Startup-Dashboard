# 📊 Startup Funding Analysis Dashboard

Explore startup funding trends and investor activity through an interactive dashboard built with Streamlit.

**Analyze funding at a glance, explore individual startups, and discover the investment history of selected investors.**

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Charts-Plotly-3F4F75?logo=plotly&logoColor=white)

---

## 📌 Overview

Startup Funding Analysis is a Python web application for exploring a startup funding dataset. Its dashboard brings together summary metrics, funding trends, startup profiles, and investor activity in one place.

Choose a view from the sidebar:

- **Overall** — review aggregate funding metrics, year-over-year and month-by-month trends, and top funding lists.
  <img width="1917" height="950" alt="image" src="https://github.com/user-attachments/assets/1247fcd5-39e4-4df3-b158-0effaecb9f24" />

- **About Startup** — select a startup to view its industry, subvertical, and location information. You can also request an AI-generated introduction.
- **About Investors** — select an investor to explore recent investments, largest investments, sector allocation, and yearly investment totals.
  <img width="1917" height="767" alt="image" src="https://github.com/user-attachments/assets/cae90ee4-67da-4a1e-b840-3273e5f6422c" />
  ![Uploading image.png…]()



## ✨ Key Features

| Feature                 | Description                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Funding summary         | Displays total funding, the highest total funding for a startup, and average total funding per startup.                       |
| Funding trends          | Visualizes annual funding totals and monthly funding totals for a selected year.                                              |
| Top funding lists       | Shows leading investors, startups by total funding, and top funding rounds for a selected year.                               |
| Startup lookup          | Displays a startup's industry vertical, subvertical, and recorded city or cities.                                             |
| AI startup introduction | Optionally requests a startup introduction using Google Gemini.                                                               |
| Investor lookup         | Shows recent deals, the investor's largest startup investment, top investments, sector allocation, and year-over-year totals. |

## 🧰 Technology

- **Python** — application language
- **Streamlit** — interactive web interface
- **Pandas** and **NumPy** — data loading and analysis
- **Plotly Express** — interactive charts
- **LangChain Google GenAI** — optional Gemini-powered startup introductions

## 🚀 Getting Started

### Requirements

- Python installed on your machine
- Dependencies listed in [`requirements.txt`](requirements.txt)

### Installation

From the project root, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks environment activation, install using the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Run the dashboard

```powershell
python -m streamlit run startup.py
```

Open the local URL printed by Streamlit, typically <http://localhost:8501>.

## ⚙️ Optional Gemini Configuration

The startup lookup can request an AI-generated introduction. To enable it, create a `.env` file in the project root and add your Google AI Studio API key:

```dotenv
GOOGLE_API_KEY=your_google_api_key
```

The rest of the dashboard works without this optional feature. Keep your API key private and do not commit `.env` to version control.

## 🗃️ Dataset

The app loads [`Dataset/startup_funding_cleaned2.csv`](Dataset/startup_funding_cleaned2.csv) when [`Data_fetch.py`](Data_fetch.py) is imported. The repository also contains the original and intermediate CSV files.

The primary CSV must include these column names:

| Column              | Used for                                               |
| ------------------- | ------------------------------------------------------ |
| `Startup Name`      | Startup selection and funding totals                   |
| `Date`              | Annual and monthly funding trends                      |
| `Amount in USD`     | Funding metrics and investment charts                  |
| `Investors Name`    | Investor selection and activity                        |
| `Industry Vertical` | Startup and investor sector analysis                   |
| `SubVertical`       | Startup profile details                                |
| `City`              | Startup location details and recent investment records |
| `Investement Type`  | Funding round details                                  |

The application drops rows with missing values and parses `Date` to derive year and month values. If you replace the dataset, preserve the expected column names and keep the file at the path above.

## 📁 Project Structure

```text
.
├── Data_fetch.py                       # Loads data and provides dashboard analyses
├── startup.py                          # Streamlit app entry point and page routing
├── requirements.txt                    # Python dependencies
└── Dataset/
    ├── startup_funding.csv             # Original dataset
    ├── startup_funding_cleaned.csv     # Intermediate cleaned dataset
    └── startup_funding_cleaned2.csv    # Dataset used by the application
```
