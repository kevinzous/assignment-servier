from typing import List

import pandas as pd


def is_drug_mentionned(drug: str, title: str) -> bool:
    """
    Returns true if drug is contained in the title, case insensitive
    """
    return drug.lower() in title.lower()


def clean_df(
    df: pd.DataFrame,
    key_cols: List[str],
) -> pd.DataFrame:
    """
    Drop rows containing missing values in the columns defined in key_cols
    """
    return df.dropna(axis=0, inplace=True, subset=key_cols)
