import yfinance as yf
from datetime import datetime

COMPANY = yf.Ticker("SIE.DE")
COLUMN_MAPPING = {
    "current_assets": ["Current Assets", "Total Current Assets"],
    "current_liabilities": ["Current Liabilities", "Total Current Liabilities"],
    "cash_equivalents": ["Cash And Cash Equivalents"],
    "short_term_investments": [
        "Other Short Term Investments",
        "Short Term Investments",
        "Marketable Securities",
    ],
    "cash_and_investments": [
        "Cash Cash Equivalents And Short Term Investments",
        "Cash And Short Term Investments",
    ],
    "restricted_cash": ["Restricted Cash"],
    "current_debt": [
        "Current Debt And Capital Lease Obligation",
        "Current Debt",
        "Current Capital Lease Obligation",
    ],
    "total_debt": [
        "Total Debt",
        "Long Term Debt And Capital Lease Obligation",
    ],
    "minority_interest": ["Minority Interest"],
    "preferred_stock": ["Preferred Stock Equity"],
}

CURRENT_YEAR = datetime.now().year

PERIOD_LABELS = {
    "0q": "Current Quarter",
    "+1q": "Next Quarter",
    "0y": f"Current Year ({CURRENT_YEAR})",
    "+1y": f"Next Year ({CURRENT_YEAR + 1})",
}

COLORS = {
    "red": "#B22222",
    "blue": "#0070BB",
    "green": "#004525",
    "gray": "#9E9E9E",
}

COLOR_RATINGS = {
    "Strong Buy": "#004525",
    "Buy": "#03C03C",
    "Hold": "#E4D00A",
    "Underperform": "#CC5500",
    "Strong Sell": "#B22222",
}
