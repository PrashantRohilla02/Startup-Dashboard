# Startup Funding Analysis Dashboard

A comprehensive Streamlit-based dashboard for analyzing startup funding data with interactive visualizations and insights.

## Features

### Overall Analysis
- **Total Investment Amount** - Sum of all investments
- **Maximum Funding** - Highest single investment amount across startups
- **Average Funding** - Average investment per startup
- **Year-over-Year (YoY) Investment Trends** - Track investment patterns across years
- **Month-over-Month (MoM) Investment** - Analyze seasonal investment trends
- **Top Investors** - Identify the most active and largest investors
- **Top Startups by Funding** - Discover which startups received the most funding
- **Top Performers** - See which startups performed best in each year

### Startup Analysis
- **Startup Details** - Get AI-powered summaries of startups using Hugging Face API
- **Industry Vertical Classification** - View industry and sub-vertical categories
- **Location Information** - See where the startup operates

### Investor Analysis
- **Recent Investments** - Track the latest investments by an investor
- **Biggest Investments** - Identify which startups received the most funding from an investor
- **Investment Distribution** - Visualize investments across different industry sectors
- **Year-over-Year Investment Trends** - Monitor investor activity over time

## Tech Stack

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Plotly** - Interactive visualizations
- **Matplotlib** - Static plots
- **Hugging Face Hub** - API integration for AI-powered summaries

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/PrashantRohilla02/Startup-Dashboard.git
cd Startup-Funding_strm
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your Hugging Face API key:
```
HF_API_KEY=your_hugging_face_api_key_here
```

To get your Hugging Face API key, visit [Hugging Face Settings](https://huggingface.co/settings/tokens)

## Usage

Run the Streamlit application:
```bash
streamlit run startup.py
```

The application will open in your default web browser at `http://localhost:8501`

### Navigation

1. **Overall** - View aggregate funding statistics and trends
2. **About Startup** - Select a startup to view detailed information
3. **About Investors** - Select an investor to view their investment portfolio

## Project Structure

```
Startup-Funding_strm/
├── startup.py                  # Main Streamlit application
├── Data_fetch.py              # Data processing and analysis functions
├── Dataset/
│   ├── startup_funding.csv
│   ├── startup_funding_cleaned.csv
│   └── startup_funding_cleaned2.csv
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

## Key Files

### `startup.py`
Main application file that sets up the Streamlit interface with three analysis sections:
- Overall analysis dashboard
- Startup information page
- Investor information page

### `Data_fetch.py`
Contains all data processing and analysis functions including:
- Data loading and preprocessing
- Aggregate calculations (total, max, average)
- Time-series analysis (YoY, MoM)
- Visualization functions
- API integration for startup summaries

## Data Format

The CSV files should contain the following columns:
- `Startup Name` - Name of the startup
- `Date` - Investment date
- `Amount in USD` - Investment amount
- `Investors Name` - Name(s) of investors (comma-separated)
- `Industry Vertical` - Main industry category
- `SubVertical` - Sub-category
- `City` - Location
- `Investment Type` - Type of investment round

## Features in Detail

### Number Formatting
Large numbers are automatically formatted for readability:
- Billions, Millions, Thousands

### Interactive Filters
- Year selection for MoM analysis
- Dynamic dropdown selections for startups and investors

### Data Visualizations
- Bar charts for YoY trends
- Pie charts for sector distribution
- Data tables for detailed information
- Plotly interactive charts for better exploration

## Requirements

See `requirements.txt` for complete dependencies:
- streamlit
- pandas
- numpy
- matplotlib
- plotly
- requests
- python-dotenv
- huggingface-hub

## Configuration

The application uses environment variables for sensitive information:
- `HF_API_KEY` - Required for AI-powered startup summaries

Create a `.env` file in the project root and add your API key.

## Notes

- Data is cleaned and null values are removed during initialization
- The application converts date strings to datetime objects automatically
- Large datasets are efficiently grouped and aggregated for performance

## Future Enhancements

- Add export functionality for reports
- Implement caching for API calls
- Add more filtering options
- Include funding round analysis
- Add predictive analytics

## License

This project is open source and available on GitHub.

## Contact

For questions or suggestions, please reach out via GitHub issues.
