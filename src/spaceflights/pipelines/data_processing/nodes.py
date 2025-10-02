import pandas as pd

def _is_true(x: pd.Series) -> pd.Series:
    return x == 't'

def _parse_percentage(x: pd.Series) -> pd.Series:
    return x.str.replace('%', '').astype(float)

def _parse_money(x: pd.Series) -> pd.Series:
    x.str.replace('$', '').str.replace(',', '').astype(float)

def preprocess_companies(df: pd.DataFrame) -> pd.DataFrame:
    df['iata_approved'] = _is_true(df['iata_approved'])
    df['company_rating'] = _parse_percentage(df['company_rating'])
    return df

def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    df['d_check_complete'] = _is_true(df['d_check_complete'])
    df['moon_clearance_complete'] = _is_true(df['moon_clearance_complete'])
    df['price'] = _parse_money(df['price'])
    return df