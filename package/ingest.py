import pandas as pd

from conf.config import ingest_conf


def ingest() -> pd.DataFrame:
    """
    Manually ingest source files and return list of dataframes
    """
    df_clinical_trials = pd.read_csv(
        filepath_or_buffer=ingest_conf["clinical_trials"]["path"],
        parse_dates=ingest_conf["clinical_trials"]["parse_dates"],
        dayfirst=ingest_conf["clinical_trials"]["dayfirst"],
    )
    df_drugs = pd.read_csv(filepath_or_buffer=ingest_conf["drugs"]["path"])
    df_pubmed = pd.concat(
        [
            pd.read_json("data/source/pubmed_cor.json"),
            pd.read_csv(
                filepath_or_buffer=ingest_conf["pubmed"]["path"],
                parse_dates=ingest_conf["pubmed"]["parse_dates"],
                dayfirst=ingest_conf["pubmed"]["dayfirst"],
            ),
        ]
    )
    return df_drugs, df_clinical_trials, df_pubmed
