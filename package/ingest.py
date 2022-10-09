import pandas as pd


def ingest()->pd.DataFrame:
    """
    Manually ingest source files and return list of dataframes
    """
    df_clinical_trials = pd.read_csv(
        "data/source/clinical_trials.csv", parse_dates=["date"], dayfirst=True
    )
    df_drugs = pd.read_csv("data/source/drugs.csv")
    df_pubmed = pd.concat(
        [
            pd.read_json("data/source/pubmed_cor.json"),
            pd.read_csv("data/source/pubmed.csv", parse_dates=["date"], dayfirst=True),
        ]
    )
    return df_drugs, df_clinical_trials, df_pubmed
