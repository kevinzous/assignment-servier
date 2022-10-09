# assignment-servier

## I. Python and Data Engineering

### I.1- Project layout

.
├── Makefile             ##  
├── README.md            ## README.md
├── bin                  ## entrypoints
│   └── build_graph.py
├── conf
├── data
│   └── sink             ## output data
│   └── source           ## input data
├── package              ## package
│   ├── ingest.py
│   ├── transform.py
│   └── utils.py
├── poetry.lock          ## dependencies lock
├── pyproject.toml       ## dependencies management
├── sql                  ## sql code for part 2 questions  
└── tests
    └── unit_test

### I.2- Run the pipelines

To run the pipelines, run :

```bash
poetry install
poetry run build_graph # question 3
poetry run get_journal_mentionning_most_drugs # question 4
```

### I.3- To go further

```text
Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de
telles volumétries ?
```

### I.4- To-do list

- smaller one task functions
- add more abstractions / config
- add github actions CI/CD : code linter, dryrun
- precommit hooks
- logging

### 

## II. SQL

Bigquery SQL will be the dialect used to solve the SQL-related questions.
To test the queries, run on the Bigquery web UI the [DDL query](sql/init.sql) that builds the source tables.

### Question 1

[code](sql/q1.sql)

### Question 2

[code](sql/q2.sql)
