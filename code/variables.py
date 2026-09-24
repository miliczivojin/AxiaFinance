import yfinance as yf
from datetime import datetime

COMPANY = yf.Ticker("SIE.DE")
COLUMN_MAPPING = {
    "current_assets": ["current_assets", "total_current_assets"],
    "current_liabilities": ["current_liabilities", "total_current_liabilities"],
    "cash_equivalents": ["cash_and_cash_equivalents"],
    "short_term_investments": [
        "other_short_term_investments",
        "short_term_investments",
        "marketable_securities",
    ],
    "cash_and_investments": [
        "cash_cash_equivalents_and_short_term_investments",
        "cash_and_short_term_investments",
    ],
    "restricted_cash": ["restricted_cash"],
    "current_debt": [
        "current_debt_and_capital_lease_obligation",
        "current_debt",
        "current_capital_lease_obligation",
    ],
    "total_debt": [
        "total_debt",
        "long_term_debt_and_capital_lease_obligation",
    ],
    "minority_interest": ["minority_interest"],
    "preferred_stock": ["preferred_stock_equity"],
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
