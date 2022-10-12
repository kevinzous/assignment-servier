# from pydoc import cli

from conf.config import OUTPUT_PATH, extract_conf
from package.ingest import ingest
from package.transform import get_drugs_in_journal, get_drugs_in_medium


def cli():
    """
    Generate 3 json files containing the drugs and its mentions in
    journal, pubmed and clinical trials
    """
    df_drugs, df_clinical_trials, df_pubmed = ingest()

    res_clinical_trials = get_drugs_in_medium(
        df_drugs=df_drugs,
        df_medium=df_clinical_trials,
        medium=extract_conf["clinical_trials"]["medium"],
        medium_id=extract_conf["clinical_trials"]["medium_id"],
        lookup_column=extract_conf["clinical_trials"]["lookup_column"],
    )

    res_clinical_trials.to_json(
        f'{OUTPUT_PATH}/{extract_conf["clinical_trials"]["output_name"]}.json'
    )

    res_pubmed = get_drugs_in_medium(
        df_drugs=df_drugs,
        df_medium=df_pubmed,
        medium=extract_conf["pubmed"]["medium"],
        medium_id=extract_conf["pubmed"]["medium_id"],
        lookup_column=extract_conf["pubmed"]["lookup_column"],
    )
    res_pubmed.to_json(f'{OUTPUT_PATH}/{extract_conf["pubmed"]["output_name"]}.json')
    res_journal = get_drugs_in_journal(
        df_drugs=df_drugs,
        list_df_medium=[df_pubmed, df_clinical_trials],
        list_medium=["pubmed", "clinical_trials"],
        journal_id="journal",
        list_lookup_column=["title", "scientific_title"],
    )
    res_journal.to_json("data/sink/res_journal.json")

    print("written to data/sink")
