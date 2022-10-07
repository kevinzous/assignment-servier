CREATE OR REPLACE TABLE  --IF NOT EXISTS
`MY_DATA_SET.TRANSACTION`
(date DATE, order_id STRING, client_id STRING, prop_id STRING, prod_price FLOAT64, prod_qty INT64)
AS
SELECT
    PARSE_DATE('%m/%d/%y', "01/01/20"),
    "1234",
    "999",
    "490756",
    CAST("50" AS FLOAT64),
    CAST("1" AS INT64)
UNION ALL
SELECT
    PARSE_DATE('%m/%d/%y', "01/01/20"),
    "1234",
    "999",
    "389728",
    CAST("3.56" AS FLOAT64),
    CAST("4" AS INT64)
UNION ALL
SELECT
    PARSE_DATE('%m/%d/%y', "01/01/20"),
    "3456",
    "845",
    "490756",
    CAST("50" AS FLOAT64),
    CAST("2" AS INT64)
UNION ALL
SELECT
    PARSE_DATE('%m/%d/%y', "01/01/20"),
    "3456",
    "845",
    "549380",
    CAST("300" AS FLOAT64),
    CAST("1" AS INT64)
UNION ALL
SELECT
    PARSE_DATE('%m/%d/%y', "01/01/20"),
    "3456",
    "845",
    "293718",
    CAST("10" AS FLOAT64),
    CAST("6" AS INT64);

CREATE OR REPLACE TABLE  --IF NOT EXISTS
`MY_DATA_SET.PRODUCT_NOMENCLATURE`
(product_id STRING, product_type STRING, product_name STRING)
AS
SELECT
    "490756",
    "MEUBLE",
    "Chaise"
UNION ALL
SELECT
    "389728",
    "DECO",
    "Boule de Noël"
UNION ALL
SELECT
    "549380",
    "MEUBLE",
    "Canapé"
UNION ALL
SELECT
    "293718",
    "DECO",
    "Mug"
