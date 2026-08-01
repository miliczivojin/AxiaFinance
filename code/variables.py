import yfinance as yf
from datetime import datetime

current_year = datetime.now().year

period_labels = {
    "0q": "Current Quarter",
    "+1q": "Next Quarter",
    "0y": f"Current Year ({current_year})",
    "+1y": f"Next Year ({current_year + 1})",
}

colors = {
    "red": "#B22222",
    "blue": "#0070BB",
    "green": "#004525",
    "gray": "#9E9E9E"
}

color_ratings = {
    "Strong Buy": "#004525",
    "Buy": "#03C03C",
    "Hold": "#E4D00A",
    "Underperform": "#CC5500",
    "Strong Sell": "#B22222"
}

company = yf.Ticker("UBER")
