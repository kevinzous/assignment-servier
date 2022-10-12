# from pydoc import cli

from package.ingest import ingest
from package.transform import get_drugs_in_journal, get_drugs_in_medium


def cli():
    """
    Generate 3 json files containing the drugs and its mentions in
    journal, pubmed and clinical trials
    """
    df_drugs, df_clinical_trials, df_pubmed = ingest()

    res_trials = get_drugs_in_medium(
        df_drugs=df_drugs,
        df_medium=df_clinical_trials,
        MEDIUM="clinical_trials",
        MEDIUM_ID="id",
        LOOKUP_COLUMN="scientific_title",
    )
    res_pubmed = get_drugs_in_medium(
        df_drugs=df_drugs,
        df_medium=df_pubmed,
        MEDIUM="pubmed",
        MEDIUM_ID="id",
        LOOKUP_COLUMN="title",
    )
    res_journal = get_drugs_in_journal(
        df_drugs=df_drugs,
        list_df_medium=[df_pubmed, df_clinical_trials],
        list_medium=["pubmed", "clinical_trials"],
        JOURNAL_ID="journal",
        list_lookup_column=["title", "scientific_title"],
    )

    res_journal.to_json("data/sink/res_journal.json")
    res_trials.to_json("data/sink/res_trials.json", orient="split")
    res_pubmed.to_json("data/sink/res_pubmed.json")

    print(res_journal.dtypes)
    print(res_pubmed.dtypes)

    print("write to data/sink")
