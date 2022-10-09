from typing import List

import pandas as pd

from package.utils import clean_df, is_drug_mentionned


def get_drugs_in_medium(
    df_drugs: pd.DataFrame,
    df_medium: pd.DataFrame,
    MEDIUM: str,
    MEDIUM_ID: str,
    LOOKUP_COLUMN: str,
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
    MEDIUM
        Name of the medium, will be used to populate the 
        generated column "source"
        ex : "clinical_trial","pubmed"
    MEDIUM_ID
        Column in df_medium used to identify the medium
    LOOKUP_COLUMN
        Column in df_medium in which we look for the drug name
        ex : "title", "scientific_title"  

    Returns
    -------
    Dataframe containing drugs mentionned in the defined medium
    """
    df_cartesian_product = df_drugs.merge(df_medium, how="cross")
    df_cartesian_product["is_drug_mentionned"] = df_cartesian_product.apply(
        lambda row: is_drug_mentionned(row.drug, getattr(row, LOOKUP_COLUMN)),
        axis=1,
    )
    df_res = df_cartesian_product[df_cartesian_product.is_drug_mentionned == True]
    del df_cartesian_product
    df_res["source"] = MEDIUM

    df_res.rename(
        columns={MEDIUM_ID: "medium_id", LOOKUP_COLUMN: "lookup_column"},
        inplace=True,
    )

    return df_res[["drug", "medium_id", "lookup_column", "date", "source"]]


def get_drugs_in_journal(
    df_drugs: pd.DataFrame,
    list_df_medium: List[pd.DataFrame],
    list_medium: List[str],
    MEDIUM_ID: str,
    list_lookup_column: List[str],
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
    MEDIUM
        Name of the medium, will be used to populate the 
        generated column "source"
        ex : "clinical_trial","pubmed"
    MEDIUM_ID
        Column in df_medium used to identify the medium
    LOOKUP_COLUMN
        Column in df_medium in which we look for the drug name
        ex : "title", "scientific_title"  

    Returns
    -------
    Dataframe containing drugs mentionned in the defined medium
    Get the drugs mentionned in the journals
    """
    assert len(list_medium) == len(list_df_medium) == len(list_lookup_column)

    df_concat = pd.concat(
        [
            get_drugs_in_medium(
                df_drugs=df_drugs,
                df_medium=df_medium,
                MEDIUM=MEDIUM,
                MEDIUM_ID=MEDIUM_ID,
                LOOKUP_COLUMN=LOOKUP_COLUMN,
            ).drop_duplicates()
            # iterate through the number of mediums
            for df_medium, MEDIUM, LOOKUP_COLUMN in zip(
                list_df_medium, list_medium, list_lookup_column
            )
        ]
    )

    df_concat = df_concat.drop(columns=["lookup_column", "source"]).drop_duplicates()

    return df_concat
