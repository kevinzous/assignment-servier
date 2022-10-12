OUTPUT_PATH = "data/sink"

ingest_conf = dict(
    clinical_trials=dict(
        name="clinical_trials",
        path="data/source/clinical_trials.csv",
        parse_dates=["date"],
        dayfirst=True,
    ),
    pubmed=dict(
        name="clinical_trials",
        path="data/source/pubmed.csv",
        parse_dates=["date"],
        dayfirst=True,
    ),
    drugs=dict(
        name="drugs",
        path="data/source/drugs.csv",
    ),
)

extract_conf = dict(
    clinical_trials=dict(
        medium="clinical_trials",
        medium_id="id",
        lookup_column="scientific_title",
        output_name="res_clinical_trials",
    ),
    pubmed=dict(
        medium="pubmed",
        medium_id="id",
        lookup_column="title",
        output_name="res_pubmed",
    ),
)


