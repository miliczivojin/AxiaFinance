import pandas as pd


def calculate_scale(value):
    value = abs(value)

    if value >= 1e12:
        return 1e12, "Trillions"
    elif value >= 1e9:
        return 1e9, "Billions"
    elif value >= 1e6:
        return 1e6, "Millions"
    elif value >= 1e3:
        return 1e3, "Thousands"

    return 1, ""


def format_value(value):
    if pd.isna(value):
        return "-"

    scale, unit = calculate_scale(value)
    return f"{value / scale:.2f}{unit[0] if unit else ""}"
