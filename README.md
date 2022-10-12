# assignment-servier

## I. Python and Data Engineering

### I.1- Project layout

```bash
.
├── Makefile                                    
├── README.md                                 ## README.md
├── bin                                       ## entrypoints
│   └── build_graph.py                        ## question 3
│   └── get_journal_mentionning_most_drugs.py ## question 4
├── conf                                      
├── data                                      
│   └── sink                                  ## output data
│   └── source                                ## input data
├── package                                   ## package
│   ├── ingest.py                             
│   ├── transform.py                          
│   └── utils.py                              
├── poetry.lock                               ## dependencies management
├── pyproject.toml                            
├── sql                                       ## sql code for part 2 questions  
└── tests                                     
    └── unit_test                             
```

### I.2- Run the pipelines

To run the pipelines, first install the environment :

```bash
## install dependencies
poetry install
## clean output files if pipelines were run                                
make clean
```

Question 3

```bash
poetry run build_graph
# cat data/sink/res_journal.json # run to see results 
# cat data/sink/res_pubmed.json # run to see results 
# cat data/sink/res_clinical_trials.json # run to see results 
```

Question 4

```bash
poetry run get_journal_mentionning_most_drugs 
# cat data/sink/res_journal_mentionning_most_drugs.json # run to see results 
```

### I.3- To go further

```text
Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il 
puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou
millions de fichiers par exemple) ?
Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, 
pour prendre en considération de telles volumétries ?
```

- small optimizations :
  - load data/columns only related to business needs
  - use efficient less memory-intensive data types like ```int64``` or ```categorical``` instead of ```object```
  - use more efficient storage format like column-oriented format parquet with ```pandas.read_parquet``` and ```pandas.Dataframes.to_parquet```
  - leverage chunking : split files into smaller "chunks"
  
    ```python
    with pd.read_csv(FILENAME, chunksize=CHUNKSIZE) as reader:
      for chunk in reader:
          transform(chunk)
    ```

- structural optimizations :
  - adopt a cloud solution
  - leverage a cloud service that handles big volumes/ distributed computing : Dataproc(Spark), Dataflow, Bigquery

### I.4- To-do list

- smaller one-task functions
- more clean management of config data
- add github actions CI/CD : code linter, dryrun
- precommit hooks
- logging
- more unit tests/ integration tests
- management of errors/exceptions through a quarantine zone/ data quality checks 

## II. SQL

Bigquery SQL will be the dialect used to solve the SQL-related questions.
To test the queries, run on the Bigquery web UI the [DDL query](sql/init.sql) that builds the source tables.

### Question 1

[code](sql/q1.sql)

### Question 2

[code](sql/q2.sql)
