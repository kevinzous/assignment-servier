#!/usr/bin/env python3
from bin.build_graph import cli as cli_build_graph
from bin.get_journal_mentionning_most_drugs import cli as cli_get_journal_mentionning_most_drugs


def test_build_graph():
    cli_build_graph()

def test_get_journal_mentionning_most_drugs():
    cli_get_journal_mentionning_most_drugs()
