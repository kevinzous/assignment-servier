import pandas as pd

from package.utils import clean_df, is_drug_mentionned


def get_journal_mentionning_most_drugs() -> str:
    """
    Need to be present : data/sink/res_journal.json
    Returns
    -------
    journal mentionning the most drugs in all medium
    """
    df_journal = pd.read_json("data/sink/res_journal.json")
    df_group_by = (
        df_journal.groupby("medium_id").drug.nunique().sort_values(ascending=False)
    )
    journal = df_group_by.head(1).reset_index().rename(columns={"drug":"distinct_count_drugs"})
    return journal
