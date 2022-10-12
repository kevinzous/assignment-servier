from package.adhoc import get_journal_mentionning_most_drugs


def cli():
    """
    Generate 1 json file containing the journal mentionning the most drugs.
    If several journals have the same count, the first journal in the alphabetical
    order is retrieved.
    """
    res = get_journal_mentionning_most_drugs()
    res.to_json("data/sink/res_journal_mentionning_most_drugs.json")
    print("written to data/sink")
