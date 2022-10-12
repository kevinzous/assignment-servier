from typing import List

import pandas as pd

from package.utils import clean_df, is_drug_mentionned


def get_drugs_in_medium(
    df_drugs: pd.DataFrame,
    df_medium: pd.DataFrame,
    medium: str,
    medium_id: str,
    lookup_column: str,
) -> pd.DataFrame:
    """
    Parameters
    ----------
    df_drugs
        Dataframe containing the drugs
        Needs to have following column(s): "drug"
    df_medium
        Dataframe containing the medium
        Needs to have following column(s): "date"
    medium
        Name of the medium, will be used to populate the
        generated column "source"
        ex : "clinical_trial","pubmed"
    medium_id
        Column in df_medium used to identify the medium
    lookup_column
        Column in df_medium in which we look for the drug name
        ex : "title", "scientific_title"

    Returns
    -------
    Dataframe containing drugs mentionned in the defined medium
    """
    df_cartesian_product = df_drugs.merge(df_medium, how="cross")
    df_cartesian_product["is_drug_mentionned"] = df_cartesian_product.apply(
        lambda row: is_drug_mentionned(row.drug, getattr(row, lookup_column)),
        axis=1,
    )
    df_res = df_cartesian_product[df_cartesian_product.is_drug_mentionned == True]
    del df_cartesian_product
    df_res["source"] = medium

    df_res.rename(
        columns={medium_id: "medium_id", lookup_column: "lookup_column"},
        inplace=True,
    )

    return df_res[["drug", "medium_id", "lookup_column", "date", "source"]]


def get_drugs_in_journal(
    df_drugs: pd.DataFrame,
    list_df_medium: List[pd.DataFrame],
    list_medium: List[str],
    journal_id: str,
    list_lookup_column: List[str],
) -> pd.DataFrame:
    """
    Parameters
    ----------
    df_drugs
        Dataframe containing the drugs
        Needs to have following column(s): "drug"
    list_df_medium
        list of dataframe containing the medium
        All dataframe need to have following column(s): "date"
    list_medium
        List of media name
        ex : "clinical_trial","pubmed"
    journal_id
        Column in df_medium used to identify the journal
    list_lookup_column
        List of columns in df_medium in which we look for the drug name
        ex : "title", "scientific_title"

    Returns
    -------
    Dataframe containing the drugs mentionned in the journals in all specified media
    """
    assert len(list_medium) == len(list_df_medium) == len(list_lookup_column)

    df_concat = pd.concat(
        [
            get_drugs_in_medium(
                df_drugs=df_drugs,
                df_medium=df_medium,
                medium=MEDIUM,
                medium_id=journal_id,
                lookup_column=LOOKUP_COLUMN,
            ).drop_duplicates()
            # iterate through the number of mediums
            for df_medium, MEDIUM, LOOKUP_COLUMN in zip(
                list_df_medium, list_medium, list_lookup_column
            )
        ]
    )

    df_concat = df_concat.drop(columns=["lookup_column", "source"]).drop_duplicates()

    return df_concat
