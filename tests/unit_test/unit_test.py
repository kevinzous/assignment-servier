#!/usr/bin/env python3
from pandas import read_csv

from bin.build_graph import cli as cli_build_graph
from bin.get_journal_mentionning_most_drugs import (
    cli as cli_get_journal_mentionning_most_drugs,
)


def test_build_graph():
    cli_build_graph()


def test_get_journal_mentionning_most_drugs():
    cli_get_journal_mentionning_most_drugs()


def test_data_read():
    read_csv("data/source/pubmed.csv")
    # read_json("data/source/pubmed.json")
    read_csv("data/source/drugs.csv")
    read_csv("data/source/clinical_trials.csv")
