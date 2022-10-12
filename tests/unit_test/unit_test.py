#!/usr/bin/env python3
from bin.build_graph import cli as cli_build_graph
from bin.get_journal_mentionning_most_drugs import (
    cli as cli_get_journal_mentionning_most_drugs,
)

import pytest
from pandas import read_json,read_csv
def test_build_graph():
    cli_build_graph()


def test_get_journal_mentionning_most_drugs():
    cli_get_journal_mentionning_most_drugs()

def test_data_json():
    with pytest.raises(FileNotFoundError):
        read_json("data/source/pubmed_cor.json")
    with pytest.raises(json.decoder.JSONDecodeError):
        # only show the first error
        read_json("data/source/pubmed_cor.json")
        read_json("data/source/pubmed_cor.yaml")

# def test_data_json():
#     with pytest.raises(FileNotFoundError):
#         read_json(file_path="data/source/pubmed.json")
#     with pytest.raises(json.decoder.JSONDecodeError):
#         # only show the first error
#         read_json(file_path="source/data/sample_invalid.json")
#         read_json(file_path="source/data/sample_invalid.yaml")
            