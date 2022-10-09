# assignment-servier



## I. Python and Data Engineering
.
├── Makefile             ##  
├── README.md            ##
├── bin
│   └── build_graph.py
├── conf
├── data
│   └── sink
│   └── source
├── package
│   ├── __init__.py
│   ├── ingest.py
│   ├── transform.py
│   └── utils.py
├── poetry.lock
├── pyproject.toml
├── sql
│   ├── init.sql
│   ├── q1.sql
│   └── q2.sql
└── tests
    └── unit_test
        └── unit_test.py

## II. SQL

Bigquery SQL will be the dialect used to solve the SQL-related questions.
To test the queries, run on the Bigquery web UI the [DDL query](sql/init.sql) that builds the source tables.

### Question 1

[code](sql/q1.sql)

### Question 2

[code](sql/q2.sql)
